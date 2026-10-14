# UNIT-X9 — Highway Collapse

Jogo de plataforma e ação 16 bits, feito em HTML5 Canvas e JavaScript puro, sem bibliotecas, sprites externos ou serviços de rede.

**Jogar:** https://ktzito.github.io/unit-x9-highway-collapse/

## Controles

| Ação | Teclado | Celular |
| --- | --- | --- |
| Andar | A / D ou setas | ◀ ▶ |
| Agachar | S ou seta ↓ | ▼ |
| Pular | Espaço ou Z | JUMP |
| Dash | Shift ou X | DASH |
| Atirar / carregar tiro | C ou J (segurar para carregar) | FIRE |
| Pausar / retomar | P ou Esc | PAUSE / PLAY |

## O que mudou na v1.2

- Agachamento com sprite e área de dano reduzida.
- Salto com *coyote time* e *jump buffer*, melhorando a resposta perto das bordas e ao aterrissar.
- Ciclo de corrida sincronizado ao deslocamento real do personagem.
- Três itens de recuperação de energia (6 HP, até o máximo).
- Pause, retomada e pausa automática ao sair da aba.
- Indicador numérico de HP e barra de progresso da fase.
- Cenário noturno com painéis e iluminação neon.
- Aviso visual do disparo de Vanguard e dano de contato condicionado à colisão real.
- Motos inimigas deixam de perseguir cegamente sobre trechos sem pista.

## Publicação e testes

O workflow `.github/workflows/publicar.yml` valida a estrutura HTML e a sintaxe JavaScript, depois publica no GitHub Pages. A branch de publicação é `main`.

Os testes completos de jogabilidade podem ser executados localmente com Playwright/Chromium. Os testes estruturais no GitHub **não** substituem testes interativos em um navegador real.
