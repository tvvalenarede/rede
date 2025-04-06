<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TVVALENAREDE - REDE SOCIAL </title>
<link rel="icon" type="image/png" href="https://github.com/tvvalenarede/bonani3/raw/main/logocerto2025.png">
    <link rel="shortcut icon" href="https://github.com/tvvalenarede/bonani3/raw/main/logocerto2025.png" type="image/png">
    
    <!-- Ícone do site -->
    <link rel="icon" href="logo192.png" type="image/png">
    <link rel="apple-touch-icon" href="logo192.png">
    <meta name="theme-color" content="#ffffff">

    <!-- Manifest para Progressive Web App -->
    <link rel="manifest" href="manifest.json">

    <style>
        :root {
            --primary: #2A3B47;
            --secondary: #B38E5D;
            --accent: #FF6B00;
            --orange: #FF8C00;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', system-ui;
        }

        body {
            background: #f9f9f9;
            line-height: 1.6;
        }

        .main-header {
            background: var(--primary);
            color: white;
            text-align: center;
            padding: 2rem 1rem;
            border-bottom: 3px solid var(--secondary);
        }

        .main-header h1 {
            font-size: 2.2rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
        }

        .grid-container {
            display: grid;
            grid-template-columns: 1fr 3fr 1fr;
            gap: 2rem;
            padding: 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }

        .sidebar {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .nav-button {
            display: block;
            width: 100%;
            padding: 1rem;
            margin-bottom: 1rem;
            background: var(--primary);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            transition: transform 0.3s, box-shadow 0.3s;
            text-align: center;
        }

        .nav-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            background: var(--secondary);
        }

        .main-content {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .social-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }

        .social-card {
            background: var(--primary);
            color: white;
            padding: 1.5rem;
            border-radius: 10px;
            text-align: center;
            transition: transform 0.3s;
        }

        .social-card:hover {
            transform: scale(1.05);
            background: var(--secondary);
        }

        .contact-form {
            background: var(--primary);
            padding: 2rem;
            border-radius: 10px;
            color: white;
        }

        .contact-form input,
        .contact-form textarea {
            width: 100%;
            padding: 0.8rem;
            margin: 0.5rem 0;
            border: 2px solid var(--secondary);
            border-radius: 5px;
            background: rgba(255,255,255,0.9);
        }

        .contact-form button {
            background: var(--secondary);
            color: white;
            padding: 1rem 2rem;
            border: none;
            border-radius: 5px;
            width: 100%;
            font-size: 1.1rem;
            cursor: pointer;
            transition: background 0.3s;
        }

        .contact-form button:hover {
            background: var(--accent);
        }

        .fixed-button {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: var(--accent);
            color: white;
            padding: 1rem 2rem;
            border-radius: 30px;
            text-decoration: none;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            transition: transform 0.3s;
            z-index: 1000;
        }

        .fixed-button-left {
            position: fixed;
            bottom: 20px;
            left: 20px;
            background: var(--orange);
            color: white;
            padding: 1rem 2rem;
            border-radius: 30px;
            text-decoration: none;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            transition: transform 0.3s;
            z-index: 1000;
        }

        .fixed-button:hover,
        .fixed-button-left:hover {
            transform: translateY(-3px);
            filter: brightness(1.1);
        }

        @media (max-width: 768px) {
            .grid-container {
                grid-template-columns: 1fr;
                padding: 1rem;
            }

            .sidebar {
                order: -1;
            }

            .main-header h1 {
                font-size: 1.8rem;
            }

            .fixed-button,
            .fixed-button-left {
                padding: 0.8rem 1.5rem;
                font-size: 0.9rem;
                bottom: 10px;
            }
        }
    </style>
</head>
<body>
    <!-- Cabeçalho com o logo e título -->
    <header class="main-header">
        <img src="https://github.com/tvvalenarede/bonani3/raw/main/logocerto2025.png" alt="Logo">
        <h1>TVVALENAREDE - REDE SOCIAL</h1>
    </header>

    <div class="grid-container">
        <!-- Sidebar Esquerda -->
        <div class="sidebar">
            <a href="https://www.youtube.com/watch?v=jfXF8m-zAcM&t=894s" class="nav-button">FUTEBOL ARQUIVO</a>
            <a href="https://www.youtube.com/watch?v=uP2KGb9CxkY&t=3473s" class="nav-button">FUTEBOL LIVE</a>
            <a href="https://www.youtube.com/watch?v=KjxwzR0Gf5Q" class="nav-button">TVVALENAREDE1NOTÍCIAS</a>
            <a href="https://www.youtube.com/watch?v=896YlUSRYdE" class="nav-button">TELETON ANIMADO</a>
            <a href="https://www.youtube.com/watch?v=1zgB6ksHk0M" class="nav-button">JEQUITI ANIMADO</a>
            <a href="https://www.youtube.com/watch?v=z2j0Yzf8Myk&t=34s" class="nav-button">PREMIAÇÃO ACEESP</a>
        </div>

        <!-- Conteúdo Principal -->
        <div class="main-content">
            <div class="social-grid">
                <a href="https://made-center7.webnode.page" class="social-card">MADE CENTER</a>
                <a href="https://www.facebook.com/groups/454428378011062?locale=pt_BR" class="social-card">GRUPO MADE CENTER</a>
                <a href="https://bar-do-osmar-de-taubate-s-p.webnode.page/" class="social-card">BAR DO OSMAR</a>
                <a href="http://www.youtube.com/tvvalenarede" class="social-card">CASA 3 IRMÃOS</a>
                <a href="https://tvvalenarede.webnode.page/?_gl=1*1p8g9b5*_gcl_au*MTI0NjU5NzMzNS4xNzQxNzI2MjQ1LjkzMjUyOTk2Mi4xNzQyMzA0NTI5LjE3NDIzMDQ1Mjg." class="social-card">ADVOGADOS ASSOCIADOS J.E.C.S</a>
                <a href="https://serginhos-centro-automotivo-de-taubate.webnode.page/" class="social-card">SERGINHO PNEUS</a>
            </div>

            <form class="contact-form" id="meuFormulario" action="https://formsubmit.co/tvrbrazil@gmail.com" method="POST">
                <input type="text" id="nome" name="Nome" placeholder="Nome" required>
                <input type="email" id="email" name="E-mail" placeholder="E-mail" required>
                <textarea id="mensagem" name="Mensagem" rows="5" placeholder="Mensagem" required></textarea>
                <input type="hidden" name="_subject" value="Nova mensagem do site">
                <button type="submit">ENVIAR MENSAGEM</button>
            </form>
        </div>

        <!-- Sidebar Direita -->
        <div class="sidebar">
            <a href="https://www.facebook.com/?locale=pt_BR" class="nav-button">FACEBOOK</a>
            <a href="https://www.facebook.com/tvvalenarede2" class="nav-button">FACEBOOK2</a>
            <a href="https://www.instagram.com/tvvalenarede?igsh=aWF0bjdueGR5N3cw" class="nav-button">INSTAGRAM1</a>
            <a href="https://www.instagram.com/tvvalenarede2/" class="nav-button">INSTAGRAM2</a>
            <a href="http://youtube.com/tvvalenarede" class="nav-button">YOUTUBE</a>
            <a href="https://www.tiktok.com/@tvvalenarede?_t=ZM-8uwnC2d12ZD&_r=1" class="nav-button">TIKTOK</a>
        </div>
    </div>

    <!-- Botões Fixos -->
    <a href="https://made-center-taubate.webnode.page/produtos/" class="fixed-button">ACESSE MADE CENTER</a>
    <a href="https://tvvalenarede.webnode.page/?_gl=1*tgfs5g*_gcl_au*MTI0NjU5NzMzNS4xNzQxNzI2MjQ1LjkzMjUyOTk2Mi4xNzQyMzA0NTI5LjE3NDIzMDQ1Mjg." class="fixed-button-left">J.E.C.S</a>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const formulario = document.getElementById('meuFormulario');

            formulario.addEventListener('submit', (e) => {
                e.preventDefault();

                // Validação do e-mail
                const email = formulario.email.value;
                if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                    alert('Por favor, insira um e-mail válido!');
                    return;
                }

                // Validação da mensagem
                if (formulario.mensagem.value.trim().length < 10) {
                    alert('A mensagem deve ter pelo menos 10 caracteres!');
                    return;
                }

                // Confirmação de envio
                if (confirm('Deseja realmente enviar a mensagem?')) {
                    formulario.submit();
                    alert('Mensagem enviada com sucesso!');
                    formulario.reset();
                }
            });
        });
    </script>
</body>
</html>
