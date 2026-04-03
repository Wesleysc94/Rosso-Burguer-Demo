/**
 * extract-frames.cjs — Extrai frames do burger-assembly.mp4 como WebP
 * Técnica Apple-style: image sequence ao invés de video.currentTime scrubbing
 */
const { execFileSync, spawnSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const FFMPEG  = path.join(__dirname, '../node_modules/ffmpeg-static/ffmpeg.exe');
const FFPROBE = path.join(path.dirname(FFMPEG), 'ffprobe.exe');
const INPUT   = path.join(__dirname, '../assets/burger-assembly.mp4');
const OUT_DIR = path.join(__dirname, '../assets/frames');

if (!fs.existsSync(INPUT)) { console.error('Video não encontrado:', INPUT); process.exit(1); }

// Criar pasta output
fs.mkdirSync(OUT_DIR, { recursive: true });

// Verificar ffprobe
const hasFfprobe = fs.existsSync(FFPROBE);
console.log('ffmpeg:', FFMPEG);
console.log('ffprobe:', hasFfprobe ? FFPROBE : 'NÃO ENCONTRADO — usando valor fixo');

// Pegar duração do vídeo
let duration = 8; // fallback
if (hasFfprobe) {
  try {
    const probe = spawnSync(FFPROBE, [
      '-v', 'quiet', '-show_entries', 'format=duration',
      '-of', 'default=noprint_wrappers=1:nokey=1', INPUT
    ], { encoding: 'utf8' });
    duration = parseFloat(probe.stdout.trim());
    console.log('Duração detectada:', duration.toFixed(2) + 's');
  } catch(e) { console.log('Usando duração fallback:', duration); }
} else {
  console.log('Usando duração fallback:', duration);
}

// Parâmetros de extração
const TOTAL_FRAMES = 100;  // 100 frames = ~12fps para 8s de vídeo
const TARGET_FPS   = (TOTAL_FRAMES / duration).toFixed(3);
const SCALE        = 'scale=1920:-2';

console.log(`\nExtraindo ${TOTAL_FRAMES} frames a ${TARGET_FPS} fps...`);
console.log(`Output: ${OUT_DIR}\n`);

// Limpar frames antigos
const existing = fs.readdirSync(OUT_DIR).filter(f => f.match(/^frame-\d+\.(webp|jpg)$/));
existing.forEach(f => fs.unlinkSync(path.join(OUT_DIR, f)));

// Executar ffmpeg — extrair como JPEG (mais compatível e leve)
const args = [
  '-i', INPUT,
  '-vf', `${SCALE},fps=${TARGET_FPS}`,
  '-q:v', '3',          // qualidade JPEG (1-31, menor = melhor)
  '-f', 'image2',
  path.join(OUT_DIR, 'frame-%03d.jpg')
];

console.log('CMD: ffmpeg ' + args.join(' ') + '\n');

const result = spawnSync(FFMPEG, args, { encoding: 'utf8', maxBuffer: 50 * 1024 * 1024 });

if (result.status !== 0) {
  console.error('ERRO ffmpeg:', result.stderr);
  process.exit(1);
}

// Contar frames gerados
const frames = fs.readdirSync(OUT_DIR).filter(f => f.match(/^frame-\d+\.jpg$/)).sort();
console.log(`✓ ${frames.length} frames gerados`);

if (frames.length === 0) {
  console.error('Nenhum frame gerado! stderr:', result.stderr);
  process.exit(1);
}

// Gerar manifest
const manifest = { totalFrames: frames.length, duration, fps: parseFloat(TARGET_FPS), files: frames };
fs.writeFileSync(path.join(OUT_DIR, 'manifest.json'), JSON.stringify(manifest, null, 2));
console.log('✓ manifest.json salvo');

// Calcular tamanho total
const totalSize = frames.reduce((acc, f) => acc + fs.statSync(path.join(OUT_DIR, f)).size, 0);
console.log(`✓ Tamanho total: ${(totalSize / 1024 / 1024).toFixed(1)} MB`);
console.log(`✓ Tamanho médio por frame: ${(totalSize / frames.length / 1024).toFixed(0)} KB`);
