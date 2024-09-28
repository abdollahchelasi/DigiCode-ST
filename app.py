import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import sqlite3
from datetime import datetime
from PIL import Image
import base64
from io import BytesIO
from pytube import YouTube
import re
import requests
from annotated_text import annotated_text


st.set_page_config(page_title="فروشگاه دیجی کد", layout="wide",page_icon="digicode.png")



with open("c.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

st.image("digicode.png",width=200)





with st.sidebar:
   menu_id = option_menu (
      menu_title=None,
      options=[ "صفحه اصلی","ساخت بازی" , "ساخت برنامه", "ارز"],
      icons=["house"],
      menu_icon="cast",
      default_index=0,
      orientation="vertical",

      styles={
         "container": {"background-color": "#ffffff","color":"#000000"},
         "nav-link-selected": {"background-color": "#9f6914","color":"#ffffff"},
         "nav-link": {"color":"#000000","font-size": "13px", "text-align": "center_y: 0.0", "margin":"0px", "--hover-color": "#e9ac4c"},

        }
    )

















if menu_id == "صفحه اصلی":

    selected = option_menu (
      menu_title=None,
      options=["چت آنلاین","راهنما","صفحه اصلی"],
      icons=["","book","house" ],
      menu_icon="cast",
      default_index=2,
      orientation="horizontal",

      styles={
         "container": {"background-color": "#ffffff","color":"#000000"},
         "nav-link-selected": {"background-color": "#9f6914","color":"#ffffff"},
         "nav-link": {"color":"#000000","font-size": "13px", "text-align": "center_y: 0.0", "margin":"0px", "--hover-color": "#e9ac4c"},

        }
    )

    if selected == "صفحه اصلی":

        
        st.markdown("# :rainbow[فروشگاه آموزشی دیجی کد یکی از بزرگترین مرجع آموزشی ساخت وب اپلیکیشن و بازی برای همه]")

        st.divider()

        annotated_text(
            "با دیجی کد ",
    ("هم بازی کن و هم بازی سازی رو یاد بگیر", "برنامه بساز و از برنامه توی دیجی کد استفاده کن"),
    " توی دیجی کد ",
    (" میتونی خیلی سریع ساخت بازی و برنامه رو یاد بگیری", "کافیه از کدهایی که قرار دادم رو استفاده کنی"),
    " اگر فروشگاه داری یا برای کسب و کار شخصیت استفاده کنی یا میخوای برای کسی وبسایتی بزنی",
    (" اگر میخوای درآمدی داشته باشی", "از کدهایی که قرار دادم میتونی استفاده کنی"),
    "توی دیجی کد",
    
    ("به صورت آنلاین هم بازی کن", "و هم از برنامه استفاده کن"),
    
   
        )
        
            


    if selected == "راهنما":

        st.warning("""
توجه : اگر میخواین کدها رو اجرا کنید و برای دیگران بفرستید کافیه تو سایت Replit ثبت نام کنید و یک پروژه streamlit ایجاد کنید و کدهایی که در اختیار شما قرار دادم رو توی پروژه قرار بدید و تغییراتی که میخواین اعمال کنید و اجرا کنید و بعد میتونید لینک وبسایت رو برای دیگران بفرستید
""") 



    if selected == "چت آنلاین":
        
        st.warning("توجه : برای مشاهده آخرین پیام ها به صفحه دیگری بروید و دوباره به همین صفحه بیایید .")

        with st.expander("چت آنلاین", expanded=True):
          
        #   st.image('g2.png')

            conn = sqlite3.connect('ch.db')
            c = conn.cursor()

            # ایجاد جدول پیام‌ها اگر وجود نداشته باشد
            c.execute('''CREATE TABLE IF NOT EXISTS messages
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT,
                        message TEXT,
                        timestamp DATETIME)''')
            conn.commit()

            # تابع افزودن پیام جدید
            def add_message(username, message):
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                c.execute("INSERT INTO messages (username, message, timestamp) VALUES (?, ?, ?)",
                          (username, message, timestamp))
                conn.commit()

            # تابع دریافت تمام پیام‌ها
            def get_messages():
                c.execute("SELECT id, username, message, timestamp FROM messages ORDER BY timestamp DESC LIMIT 100")
                return c.fetchall()

            # تابع حذف پیام
            def delete_message(message_id):
                c.execute("DELETE FROM messages WHERE id = ?", (message_id,))
                conn.commit()

            # ورود نام کاربری
            
              
            username = st.text_input(": نام خود را وارد کنید")

            # نمایش پیام‌های موجود
            messages = get_messages()
            new_message = st.text_input(": پیام خود را وارد کنید")
            ersal = st.button("ارسال") 
            
            # ورودی پیام جدید
            if ersal and username and new_message :
              
              add_message(username, new_message)
              st.rerun()
            
            elif ersal and username and new_message == "":
                # add_message(username, new_message)
                st.error("لطفا پیام‌ خو بنویس" )

            elif ersal and new_message and username == "":
                # add_message(username, new_message)
                st.error("لطفا اسم خو بنویس")


            


            st.subheader("🔻 چت آنلاین 🔻")
            st.divider()

            for msg in messages:  # بدون معکوس کردن لیست پیام‌ها
                msg_id, msg_user, msg_text, msg_timestamp = msg
                st.success(f"{msg_timestamp} 🙋🏽‍♂️ {msg_user}: 💬 {msg_text}")
                
                # افزودن دکمه برای حذف پیام
                if st.button("حذف", key=f"delete_{msg_id}"):
                    delete_message(msg_id)
                    st.rerun()

            # بستن اتصال به پایگاه داده
            conn.close()



if menu_id == "ساخت بازی":
    
    st.divider()


    c1 , c2 ,c3 = st.columns(3)

    with c1:
        with st.expander("بازی TicTakToe", expanded=True):
            st.image("Gtic.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("ساخت بازی تیک تاک تو یک بازی که با کامبیوتر بازی میکنید")
                st.image("p.png",width=20)

            if st.button("نمایش کد بازی TicTakToe"):

                st.code('''
    
import streamlit as st
import pygame
import sys
# Initialize pygame
if st.button("OK"):
    pygame.init()
    WIDTH, HEIGHT = 600, 600
    LINE_COLOR = (0, 0, 0)
    BOARD_COLOR = (255, 255, 255)
    LINE_WIDTH = 15
    ROWS, COLS = 3, 3
    SQUARE_SIZE = WIDTH // COLS
    def draw_lines():
        for i in range(1, ROWS):
            pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
            pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    def draw_figures():
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 1:
                    pygame.draw.circle(screen, (255, 0, 0), (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), SQUARE_SIZE // 3, 15)
                elif board[row][col] == 2:
                    pygame.draw.line(screen, (0, 0, 255), (col * SQUARE_SIZE + 50, row * SQUARE_SIZE + SQUARE_SIZE - 50), (col * SQUARE_SIZE + SQUARE_SIZE - 50, row * SQUARE_SIZE + 50), 15)
    def mark_square(row, col, player):
        board[row][col] = player
    def available_square(row, col):
        return board[row][col] == 0
    def check_win(player):
        
        for row in range(ROWS):
            if board[row][0] == board[row][1] == board[row][2] == player:
                return True
        
        for col in range(COLS):
            if board[0][col] == board[1][col] == board[2][col] == player:
                return True
        
        if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False
    def restart():
        global board, game_over, winner
        board = [[0] * COLS for _ in range(ROWS)]
        game_over = False
        winner = None
        screen.fill(BOARD_COLOR)
        draw_lines()
        pygame.display.update()
    def computer_move():
        
        for row in range(ROWS):
            for col in range(COLS):
                if available_square(row, col):
                    return row, col
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic-Tac-Toe")
    board = [[0] * COLS for _ in range(ROWS)]
    game_over = False
    winner = None
    player = 1
    draw_lines()
    restart_button_rect = pygame.Rect(250, 10, 100, 50)  # Define Restart button dimensions and posi
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)
                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player):
                        winner = player
                        game_over = True
                    elif all(all(cell != 0 for cell in row) for row in board):
                        game_over = True
                    else:
                        player = player % 2 + 1
                    draw_figures()
                    # Check if game is over before computer's move
                    if game_over:
                        pygame.draw.rect(screen, BOARD_COLOR, restart_button_rect)  # Clear Restart button area
                        break
                    # Computer's turn
                    comp_row, comp_col = computer_move()
                    mark_square(comp_row, comp_col, player)
                    if check_win(player):
                        winner = player
                        game_over = True
                    elif all(all(cell != 0 for cell in row) for row in board):
                        game_over = True
                    else:
                        player = player % 2 + 1
                    draw_figures()
            # Show Restart button if game is over
            if game_over:
                pygame.draw.rect(screen, (255, 255, 255), restart_button_rect)
                font = pygame.font.Font(None, 36)
                text = font.render("RESTART", True, (0, 0, 0))
                text_rect = text.get_rect(center=restart_button_rect.center)
                screen.blit(text, text_rect)
                # Display winner
                if winner:
                    win_text = f"Player {winner} wins!"
                else:
                    win_text = "It's a tie!"
                win_surface = font.render(win_text, True, (0, 0, 0))
                win_rect = win_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                screen.blit(win_surface, win_rect)
            # Handle click on Restart button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button_rect.collidepoint(event.pos):
                    restart()
                    game_over = False
        pygame.display.update()
    ''','python')
            
            st.warning("برای اجرای بازی به محیط برنامه نویسی نیاز دارید")










    with c2:
        with st.expander("بازی بیلیارد", expanded=True):
            st.image("bil.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("بازی معروف بیلیارد که میتونید با کامبیوتر بازی کنید و امتیازی هم کسب کنید")
                st.image("p.png",width=20)

            if st.button("نمایش کد بازی بیلیارد"):
                st.code('''
import streamlit.components.v1 as components


components.html("""

<html><head><base href="https://websim.ai"/>
<title>بازی بیلیارد</title>
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<style>
body, html {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background: #1a1a1a;
    font-family: 'Tahoma', Arial, sans-serif;
    touch-action: none;
    border-radius: 8px;
    direction: rtl;
}
#gameContainer {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: relative;
}
#gameCanvas {
    width: 100%;
    max-width: 300px;
    height: auto;
    aspect-ratio: 2/1;
    max-height: 150px;
    border: 2px solid #8B4513;
    border-radius: 8px;
    box-shadow: 0 0 8px rgba(0,0,0,.5);
}
#scoreBoard {
    position: absolute;
    top: 2px;
    font-size: 10px;
    font-weight: bold;
    color: #fff;
    text-shadow: 1px 1px 1px rgba(0,0,0,.5);
    background: rgba(0,0,0,0.5);
    padding: 2px;
    border-radius: 2px;
    text-align: center;
    width: 80%;
    max-width: 280px;
}
#powerMeter {
    position: absolute;
    left: 2px;
    top: 50%;
    transform: translateY(-50%);
    width: 8px;
    height: 40%;
    max-height: 100px;
    background: #444;
    border-radius: 4px;
    overflow: hidden;
}
#powerBar {
    width: 100%;
    height: 0%;
    background: linear-gradient(to top, green, yellow, red);
    transition: height 0.05s;
    position: absolute;
    bottom: 0;
}
#controls {
    position: absolute;
    bottom: 2px;
    display: flex;
    justify-content: center;
    width: 100%;
}
.btn {
    margin: 0 2px;
    padding: 6px 12px;
    font-size: 10px;
    background: #4CAF50;
    color: white;
    border: none;
    border-radius: 3px;
    cursor: pointer;
    touch-action: manipulation;
}
#directionControls {
    position: absolute;
    left: 2px;
    bottom: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.arrow {
    width: 24px;
    height: 24px;
    background: #4CAF50;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 2px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 14px;
    color: white;
    user-select: none;
}
#leftRight {
    display: flex;
    justify-content: space-between;
    width: 70px;
}
</style>
</head>
<body>
<div id="gameContainer">
    <div id="scoreBoard">نوبت شما (امتیاز: 0) | کامپیوتر (امتیاز: 0)</div>
    <canvas id="gameCanvas"></canvas>
    <div id="powerMeter"><div id="powerBar"></div></div>
    <div id="controls">
        <button id="startBtn" class="btn">شروع</button>
        <button id="shootBtn" class="btn">شلیک</button>
    </div>
    <div id="directionControls">
        <div id="arrowUp" class="arrow">↑</div>
        <div id="leftRight">
            <div id="arrowRight" class="arrow">→</div>
            <div id="arrowLeft" class="arrow">←</div>
        </div>
        <div id="arrowDown" class="arrow">↓</div>
    </div>
</div>
<script>
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const scoreBoard = document.getElementById('scoreBoard');
const powerBar = document.getElementById('powerBar');
const startBtn = document.getElementById('startBtn');
const shootBtn = document.getElementById('shootBtn');
const arrowUp = document.getElementById('arrowUp');
const arrowDown = document.getElementById('arrowDown');
const arrowLeft = document.getElementById('arrowLeft');
const arrowRight = document.getElementById('arrowRight');

let canvasWidth, canvasHeight, ballRadius, pocketRadius, railWidth;
let currentPlayer = 'human';
let gameState = 'notStarted'; // 'notStarted', 'aiming', 'powerAdjust', 'shooting', 'nextTurn'
let cueBall;
let balls = [];
let pockets = [];
let cueAngle = 0;
let cuePower = 0;
let lastPocketedBall = null;
let humanType = null; // 'solids' or 'stripes'
let computerType = null;
let humanScore = 0;
let computerScore = 0;

const friction = 0.985;
const speedMultiplier = 1.5;

class Ball {
    constructor(x, y, number) {
        this.x = x;
        this.y = y;
        this.vx = 0;
        this.vy = 0;
        this.number = number;
        this.pocketed = false;
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, ballRadius, 0, Math.PI * 2);
        ctx.fillStyle = this.getBaseColor();
        ctx.fill();
        ctx.strokeStyle = 'black';
        ctx.lineWidth = 1;
        ctx.stroke();
        ctx.closePath();

        if (this.number > 8) {
            ctx.beginPath();
            ctx.arc(this.x, this.y, ballRadius * 0.7, 0, Math.PI * 2);
            ctx.fillStyle = 'white';
            ctx.fill();
            ctx.closePath();
        }

        ctx.fillStyle = this.number === 0 || this.number > 8 ? 'black' : 'white';
        ctx.font = `bold ${ballRadius * 0.8}px Arial`;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(this.number, this.x, this.y);
    }

    getBaseColor() {
        const colors = ['#FFFFFF', '#FFFF00', '#0000FF', '#FF0000', '#800080', '#FFA500', '#008000', '#8B4513', '#000000', 
                        '#FFFF00', '#0000FF', '#FF0000', '#800080', '#FFA500', '#008000', '#8B4513'];
        return colors[this.number];
    }

    update() {
        this.x += this.vx * speedMultiplier;
        this.y += this.vy * speedMultiplier;
        this.vx *= friction;
        this.vy *= friction;

        if (this.x - ballRadius < railWidth) {
            this.x = railWidth + ballRadius;
            this.vx = -this.vx;
        } else if (this.x + ballRadius > canvasWidth - railWidth) {
            this.x = canvasWidth - railWidth - ballRadius;
            this.vx = -this.vx;
        }
        if (this.y - ballRadius < railWidth) {
            this.y = railWidth + ballRadius;
            this.vy = -this.vy;
        } else if (this.y + ballRadius > canvasHeight - railWidth) {
            this.y = canvasHeight - railWidth - ballRadius;
            this.vy = -this.vy;
        }
    }
}

function initializeBalls() {
    cueBall = new Ball(canvasWidth * 0.75, canvasHeight / 2, 0);
    balls = [cueBall];

    const startX = canvasWidth * 0.25;
    const startY = canvasHeight / 2;
    const rowOffsetX = Math.sqrt(3) * ballRadius;
    const rowOffsetY = ballRadius;

    const rackOrder = [1, 9, 10, 11, 8, 12, 13, 14, 2, 15, 3, 4, 5, 6, 7];
    let ballIndex = 0;

    for (let row = 0; row < 5; row++) {
        for (let col = 0; col <= row; col++) {
            if (ballIndex < rackOrder.length) {
                const x = startX + row * rowOffsetX;
                const y = startY + (col * 2 - row) * rowOffsetY;
                balls.push(new Ball(x, y, rackOrder[ballIndex]));
                ballIndex++;
            }
        }
    }
}

function initializePockets() {
    const pocketPositions = [
        {x: railWidth, y: railWidth},
        {x: canvasWidth / 2, y: railWidth},
        {x: canvasWidth - railWidth, y: railWidth},
        {x: railWidth, y: canvasHeight - railWidth},
        {x: canvasWidth / 2, y: canvasHeight - railWidth},
        {x: canvasWidth - railWidth, y: canvasHeight - railWidth}
    ];

    pockets = pocketPositions.map(pos => ({x: pos.x, y: pos.y}));
}

function drawTable() {
    ctx.fillStyle = '#006400';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.fillStyle = '#008000';
    ctx.fillRect(railWidth, railWidth, canvasWidth - 2 * railWidth, canvasHeight - 2 * railWidth);

    ctx.fillStyle = '#8B4513';
    ctx.fillRect(0, 0, canvasWidth, railWidth);
    ctx.fillRect(0, canvasHeight - railWidth, canvasWidth, railWidth);
    ctx.fillRect(0, 0, railWidth, canvasHeight);
    ctx.fillRect(canvasWidth - railWidth, 0, railWidth, canvasHeight);

    pockets.forEach(pocket => {
        ctx.beginPath();
        ctx.arc(pocket.x, pocket.y, pocketRadius, 0, Math.PI * 2);
        ctx.fillStyle = '#000';
        ctx.fill();
        ctx.closePath();
    });
}

function drawCue() {
    if ((gameState === 'aiming' || gameState === 'powerAdjust') && currentPlayer === 'human') {
        const cueLength = canvasWidth * 0.2;
        const cueEndX = cueBall.x - Math.cos(cueAngle) * cueLength;
        const cueEndY = cueBall.y - Math.sin(cueAngle) * cueLength;

        ctx.beginPath();
        ctx.moveTo(cueBall.x - Math.cos(cueAngle) * ballRadius, cueBall.y - Math.sin(cueAngle) * ballRadius);
        ctx.lineTo(cueEndX, cueEndY);
        ctx.strokeStyle = '#8B4513';
        ctx.lineWidth = ballRadius / 2;
        ctx.stroke();
        ctx.closePath();

        ctx.beginPath();
        ctx.arc(cueEndX, cueEndY, ballRadius / 4, 0, Math.PI * 2);
        ctx.fillStyle = '#FFF';
        ctx.fill();
        ctx.closePath();
    }
}

function checkCollisions() {
    for (let i = 0; i < balls.length; i++) {
        for (let j = i + 1; j < balls.length; j++) {
            const ball1 = balls[i];
            const ball2 = balls[j];

            const dx = ball2.x - ball1.x;
            const dy = ball2.y - ball1.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < ballRadius * 2) {
                const angle = Math.atan2(dy, dx);
                const sin = Math.sin(angle);
                const cos = Math.cos(angle);

                const vx1 = ball1.vx * cos + ball1.vy * sin;
                const vy1 = ball1.vy * cos - ball1.vx * sin;
                const vx2 = ball2.vx * cos + ball2.vy * sin;
                const vy2 = ball2.vy * cos - ball2.vx * sin;

                ball1.vx = vx2 * cos - vy1 * sin;
                ball1.vy = vy1 * cos + vx2 * sin;
                ball2.vx = vx1 * cos - vy2 * sin;
                ball2.vy = vy2 * cos + vx1 * sin;

                const overlap = ballRadius * 2 - distance;
                ball1.x -= overlap / 2 * cos;
                ball1.y -= overlap / 2 * sin;
                ball2.x += overlap / 2 * cos;
                ball2.y += overlap / 2 * sin;
            }
        }
    }
}

function checkPockets() {
    for (let ball of balls) {
        for (let pocket of pockets) {
            const dx = ball.x - pocket.x;
            const dy = ball.y - pocket.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < pocketRadius) {
                if (ball === cueBall) {
                    ball.x = canvasWidth * 0.75;
                    ball.y = canvasHeight / 2;
                    ball.vx = 0;
                    ball.vy = 0;
                    currentPlayer = currentPlayer === 'human' ? 'computer' : 'human';
                } else {
                    ball.pocketed = true;
                    lastPocketedBall = ball;
                    if (!humanType && currentPlayer === 'human') {
                        humanType = ball.number < 8 ? 'solids' : 'stripes';
                        computerType = ball.number < 8 ? 'stripes' : 'solids';
                    }
                    // Add score
                    if (currentPlayer === 'human') {
                        humanScore += 1;
                    } else {
                        computerScore += 1;
                    }
                }
            }
        }
    }
    balls = balls.filter(ball => !ball.pocketed);
}

function update() {
    updatePowerBar();

    if (gameState === 'shooting') {
        balls.forEach(ball => ball.update());
        checkCollisions();
        checkPockets();

        if (balls.every(ball => Math.abs(ball.vx) < 0.05 && Math.abs(ball.vy) < 0.05)) {
            gameState = 'nextTurn';
            setTimeout(() => {
                if (lastPocketedBall) {
                    if (lastPocketedBall.number === 8) {
                        if (currentPlayerAllPocketed()) {
                            alert(currentPlayer === 'human' ? 'شما برنده شدید!' : 'کامپیوتر برنده شد!');
                        } else {
                            alert(currentPlayer === 'human' ? 'شما باختید! توپ 8 را زود انداختید.' : 'کامپیوتر باخت! توپ 8 را زود انداخت.');
                            currentPlayer = currentPlayer === 'human' ? 'computer' : 'human';
                        }
                        resetGame();
                    } else if ((currentPlayer === 'human' && humanType === 'solids' && lastPocketedBall.number > 8) ||
                               (currentPlayer === 'human' && humanType === 'stripes' && lastPocketedBall.number < 8) ||
                               (currentPlayer === 'computer' && computerType === 'solids' && lastPocketedBall.number > 8) ||
                               (currentPlayer === 'computer' && computerType === 'stripes' && lastPocketedBall.number < 8)) {
                        currentPlayer = currentPlayer === 'human' ? 'computer' : 'human';
                    }
                } else {
                    currentPlayer = currentPlayer === 'human' ? 'computer' : 'human';
                }
                lastPocketedBall = null;
                gameState = 'aiming';
                updateScoreBoard();
                if (currentPlayer === 'computer') {
                    setTimeout(computerTurn, 500);
                }
            }, 500);
        }
    }
}

function currentPlayerAllPocketed() {
    const playerType = currentPlayer === 'human' ? humanType : computerType;
    if (playerType === 'solids') {
        return !balls.some(ball => ball.number > 0 && ball.number < 8);
    } else {
        return !balls.some(ball => ball.number > 8);
    }
}

function resetGame() {
    initializeBalls();
    currentPlayer = 'human';
    humanType = null;
    computerType = null;
    lastPocketedBall = null;
    humanScore = 0;
    computerScore = 0;
    gameState = 'aiming';
    updateScoreBoard();
}

function updatePowerBar() {
    if (gameState === 'powerAdjust') {
        cuePower += 1;
        if (cuePower > 20) cuePower = 20;
        powerBar.style.height = (cuePower / 20 * 100) + '%';
    }
}

function updateScoreBoard() {
    let playerType = '';
    if (humanType) {
        playerType = currentPlayer === 'human' ? ` (${humanType === 'solids' ? 'توپ‌های رنگی' : 'توپ‌های راه‌راه'})` : ` (${computerType === 'solids' ? 'توپ‌های رنگی' : 'توپ‌های راه‌راه'})`;
    }
    scoreBoard.innerHTML = `نوبت ${currentPlayer === 'human' ? 'شما' : 'کامپیوتر'}${playerType} | شما (امتیاز: ${humanScore}) | کامپیوتر (امتیاز: ${computerScore})`;
}

function draw() {
    ctx.clearRect(0, 0, canvasWidth, canvasHeight);
    drawTable();
    balls.forEach(ball => ball.draw());
    drawCue();
    
    requestAnimationFrame(draw);
}

function resizeCanvas() {
    const container = document.getElementById('gameContainer');
    const containerWidth = container.clientWidth;
    const containerHeight = container.clientHeight;

    const aspectRatio = 2/1; // Pool table aspect ratio (2:1 for horizontal layout)
    let newWidth, newHeight;

    if (containerWidth / containerHeight > aspectRatio) {
        // Fit to height
        newHeight = Math.min(containerHeight * 0.7, 150); // Reduced max height to 150px
        newWidth = newHeight * aspectRatio;
    } else {
        // Fit to width
        newWidth = Math.min(containerWidth * 0.8, 300);
        newHeight = newWidth / aspectRatio;
    }

    canvas.width = canvasWidth = newWidth;
    canvas.height = canvasHeight = newHeight;

    ballRadius = Math.min(canvasWidth, canvasHeight) * 0.018;
    pocketRadius = ballRadius * 1.7;
    railWidth = ballRadius * 1.8;

    initializeBalls();
    initializePockets();
}

function gameLoop() {
    update();
    draw();
    requestAnimationFrame(gameLoop);
}

function computerTurn() {
    if (currentPlayer !== 'computer') return;

    let targetBalls = balls.filter(ball => 
        (computerType === 'solids' && ball.number > 0 && ball.number < 8) ||
        (computerType === 'stripes' && ball.number > 8) ||
        (currentPlayerAllPocketed() && ball.number === 8)
    );

    if (targetBalls.length === 0) {
        targetBalls = balls.filter(ball => ball !== cueBall);
    }

    const targetBall = targetBalls[Math.floor(Math.random() * targetBalls.length)];
    
    const dx = targetBall.x - cueBall.x;
    const dy = targetBall.y - cueBall.y;
    cueAngle = Math.atan2(dy, dx);

    cueAngle += (Math.random() - 0.5) * 0.2;

    cuePower = 8 + Math.random() * 8;

    setTimeout(() => {
        cueBall.vx = Math.cos(cueAngle) * cuePower * speedMultiplier;
        cueBall.vy = Math.sin(cueAngle) * cuePower * speedMultiplier;
        gameState = 'shooting';
    }, 500);
}

window.addEventListener('resize', resizeCanvas);

// Control button event listeners
startBtn.addEventListener('click', () => {
    if (gameState === 'notStarted') {
        gameState = 'aiming';
        startBtn.textContent = 'شروع مجدد';
    } else {
        resetGame();
    }
});

shootBtn.addEventListener('click', () => {
    if (gameState === 'aiming') {
        gameState = 'powerAdjust';
    } else if (gameState === 'powerAdjust') {
        cueBall.vx = Math.cos(cueAngle) * cuePower * speedMultiplier;
        cueBall.vy = Math.sin(cueAngle) * cuePower * speedMultiplier;
        gameState = 'shooting';
        cuePower = 0;
        powerBar.style.height = '0%';
    }
});

// Arrow control event listeners
const arrowStep = 0.05;

function handleArrowControl(direction) {
    if (gameState === 'aiming' || gameState === 'powerAdjust') {
        switch(direction) {
            case 'up':
                cueAngle -= arrowStep;
                break;
            case 'down':
                cueAngle += arrowStep;
                break;
            case 'left':
                cueAngle += arrowStep;
                break;
            case 'right':
                cueAngle -= arrowStep;
                break;
        }
        cueAngle = (cueAngle + 2 * Math.PI) % (2 * Math.PI);
    }
}

function createArrowHandler(direction) {
    let intervalId = null;
    return {
        start: (event) => {
            event.preventDefault();
            handleArrowControl(direction);
            intervalId = setInterval(() => handleArrowControl(direction), 50);
        },
        stop: () => {
            if (intervalId !== null) {
                clearInterval(intervalId);
                intervalId = null;
            }
        }
    };
}

const arrowHandlers = {
    up: createArrowHandler('up'),
    down: createArrowHandler('down'),
    left: createArrowHandler('left'),
    right: createArrowHandler('right')
};

arrowUp.addEventListener('mousedown', arrowHandlers.up.start);
arrowUp.addEventListener('touchstart', arrowHandlers.up.start);
arrowDown.addEventListener('mousedown', arrowHandlers.down.start);
arrowDown.addEventListener('touchstart', arrowHandlers.down.start);
arrowLeft.addEventListener('mousedown', arrowHandlers.left.start);
arrowLeft.addEventListener('touchstart', arrowHandlers.left.start);
arrowRight.addEventListener('mousedown', arrowHandlers.right.start);
arrowRight.addEventListener('touchstart', arrowHandlers.right.start);

document.addEventListener('mouseup', () => {
    arrowHandlers.up.stop();
    arrowHandlers.down.stop();
    arrowHandlers.left.stop();
    arrowHandlers.right.stop();
});

document.addEventListener('touchend', () => {
    arrowHandlers.up.stop();
    arrowHandlers.down.stop();
    arrowHandlers.left.stop();
    arrowHandlers.right.stop();
});

resizeCanvas();
gameLoop();
</script>
</body></html>
""",height=500)

''')
            if st.button("اجرای بازی بیلیارد"):

                components.html("""

<html><head><base href="https://websim.ai"/>
<title>بازی بیلیارد 8 توپ - نسخه موبایل فارسی</title>
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<style>
body, html {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background: #1a1a1a;
    font-family: 'Tahoma', Arial, sans-serif;
    touch-action: none;
    border-radius: 8px;
    direction: rtl;
}
#gameContainer {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: relative;
}
#gameCanvas {
    width: 100%;
    max-width: 300px;
    height: auto;
    aspect-ratio: 2/1;
    max-height: 150px;
    border: 2px solid #8B4513;
    border-radius: 8px;
    box-shadow: 0 0 8px rgba(0,0,0,.5);
}
#scoreBoard {
    position: absolute;
    top: 2px;
    font-size: 10px;
    font-weight: bold;
    color: #fff;
    text-shadow: 1px 1px 1px rgba(0,0,0,.5);
    background: rgba(0,0,0,0.5);
    padding: 2px;
    border-radius: 2px;
    text-align: center;
    width: 80%;
    max-width: 280px;
}
#powerMeter {
    position: absolute;
    left: 2px;
    top: 50%;
    transform: translateY(-50%);
    width: 8px;
    height: 40%;
    max-height: 100px;
    background: #444;
    border-radius: 4px;
    overflow: hidden;
}
#powerBar {
    width: 100%;
    height: 0%;
    background: linear-gradient(to top, green, yellow, red);
    transition: height 0.05s;
    position: absolute;
    bottom: 0;
}
#controls {
    position: absolute;
    bottom: 2px;
    display: flex;
    justify-content: center;
    width: 100%;
}
.btn {
    margin: 0 2px;
    padding: 6px 12px;
    font-size: 10px;
    background: #4CAF50;
    color: white;
    border: none;
    border-radius: 3px;
    cursor: pointer;
    touch-action: manipulation;
}
#directionControls {
    position: absolute;
    left: 2px;
    bottom: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.arrow {
    width: 24px;
    height: 24px;
    background: #4CAF50;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 2px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 14px;
    color: white;
    user-select: none;
}
#leftRight {
    display: flex;
    justify-content: space-between;
    width: 70px;
}
</style>
</head>
<body>
<div id="gameContainer">
    <div id="scoreBoard">نوبت شما (امتیاز: 0) | کامپیوتر (امتیاز: 0)</div>
    <canvas id="gameCanvas"></canvas>
    <div id="powerMeter"><div id="powerBar"></div></div>
    <div id="controls">
        <button id="startBtn" class="btn">شروع</button>
        <button id="shootBtn" class="btn">شلیک</button>
    </div>
    <div id="directionControls">
        <div id="arrowUp" class="arrow">↑</div>
        <div id="leftRight">
            <div id="arrowRight" class="arrow">→</div>
            <div id="arrowLeft" class="arrow">←</div>
        </div>
        <div id="arrowDown" class="arrow">↓</div>
    </div>
</div>
<script>
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const scoreBoard = document.getElementById('scoreBoard');
const powerBar = document.getElementById('powerBar');
const startBtn = document.getElementById('startBtn');
const shootBtn = document.getElementById('shootBtn');
const arrowUp = document.getElementById('arrowUp');
const arrowDown = document.getElementById('arrowDown');
const arrowLeft = document.getElementById('arrowLeft');
const arrowRight = document.getElementById('arrowRight');

let canvasWidth, canvasHeight, ballRadius, pocketRadius, railWidth;
let currentPlayer = 'human';
let gameState = 'notStarted'; // 'notStarted', 'aiming', 'powerAdjust', 'shooting', 'nextTurn'
let cueBall;
let balls = [];
let pockets = [];
let cueAngle = 0;
let cuePower = 0;
let lastPocketedBall = null;
let humanType = null; // 'solids' or 'stripes'
let computerType = null;
let humanScore = 0;
let computerScore = 0;

const friction = 0.985;
const speedMultiplier = 1.5;

class Ball {
    constructor(x, y, number) {
        this.x = x;
        this.y = y;
        this.vx = 0;
        this.vy = 0;
        this.number = number;
        this.pocketed = false;
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, ballRadius, 0, Math.PI * 2);
        ctx.fillStyle = this.getBaseColor();
        ctx.fill();
        ctx.strokeStyle = 'black';
        ctx.lineWidth = 1;
        ctx.stroke();
        ctx.closePath();

        if (this.number > 8) {
            ctx.beginPath();
            ctx.arc(this.x, this.y, ballRadius * 0.7, 0, Math.PI * 2);
            ctx.fillStyle = 'white';
            ctx.fill();
            ctx.closePath();
        }

        ctx.fillStyle = this.number === 0 || this.number > 8 ? 'black' : 'white';
        ctx.font = `bold ${ballRadius * 0.8}px Arial`;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(this.number, this.x, this.y);
    }

    getBaseColor() {
        const colors = ['#FFFFFF', '#FFFF00', '#0000FF', '#FF0000', '#800080', '#FFA500', '#008000', '#8B4513', '#000000', 
                        '#FFFF00', '#0000FF', '#FF0000', '#800080', '#FFA500', '#008000', '#8B4513'];
        return colors[this.number];
    }

    update() {
        this.x += this.vx * speedMultiplier;
        this.y += this.vy * speedMultiplier;
        this.vx *= friction;
        this.vy *= friction;

        if (this.x - ballRadius < railWidth) {
            this.x = railWidth + ballRadius;
            this.vx = -this.vx;
        } else if (this.x + ballRadius > canvasWidth - railWidth) {
            this.x = canvasWidth - railWidth - ballRadius;
            this.vx = -this.vx;
        }
        if (this.y - ballRadius < railWidth) {
            this.y = railWidth + ballRadius;
            this.vy = -this.vy;
        } else if (this.y + ballRadius > canvasHeight - railWidth) {
            this.y = canvasHeight - railWidth - ballRadius;
            this.vy = -this.vy;
        }
    }
}

function initializeBalls() {
    cueBall = new Ball(canvasWidth * 0.75, canvasHeight / 2, 0);
    balls = [cueBall];

    const startX = canvasWidth * 0.25;
    const startY = canvasHeight / 2;
    const rowOffsetX = Math.sqrt(3) * ballRadius;
    const rowOffsetY = ballRadius;

    const rackOrder = [1, 9, 10, 11, 8, 12, 13, 14, 2, 15, 3, 4, 5, 6, 7];
    let ballIndex = 0;

    for (let row = 0; row < 5; row++) {
        for (let col = 0; col <= row; col++) {
            if (ballIndex < rackOrder.length) {
                const x = startX + row * rowOffsetX;
                const y = startY + (col * 2 - row) * rowOffsetY;
                balls.push(new Ball(x, y, rackOrder[ballIndex]));
                ballIndex++;
            }
        }
    }
}

function initializePockets() {
    const pocketPositions = [
        {x: railWidth, y: railWidth},
        {x: canvasWidth / 2, y: railWidth},
        {x: canvasWidth - railWidth, y: railWidth},
        {x: railWidth, y: canvasHeight - railWidth},
        {x: canvasWidth / 2, y: canvasHeight - railWidth},
        {x: canvasWidth - railWidth, y: canvasHeight - railWidth}
    ];

    pockets = pocketPositions.map(pos => ({x: pos.x, y: pos.y}));
}

function drawTable() {
    ctx.fillStyle = '#006400';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.fillStyle = '#008000';
    ctx.fillRect(railWidth, railWidth, canvasWidth - 2 * railWidth, canvasHeight - 2 * railWidth);

    ctx.fillStyle = '#8B4513';
    ctx.fillRect(0, 0, canvasWidth, railWidth);
    ctx.fillRect(0, canvasHeight - railWidth, canvasWidth, railWidth);
    ctx.fillRect(0, 0, railWidth, canvasHeight);
    ctx.fillRect(canvasWidth - railWidth, 0, railWidth, canvasHeight);

    pockets.forEach(pocket => {
        ctx.beginPath();
        ctx.arc(pocket.x, pocket.y, pocketRadius, 0, Math.PI * 2);
        ctx.fillStyle = '#000';
        ctx.fill();
        ctx.closePath();
    });
}

function drawCue() {
    if ((gameState === 'aiming' || gameState === 'powerAdjust') && currentPlayer === 'human') {
        const cueLength = canvasWidth * 0.2;
        const cueEndX = cueBall.x - Math.cos(cueAngle) * cueLength;
        const cueEndY = cueBall.y - Math.sin(cueAngle) * cueLength;

        ctx.beginPath();
        ctx.moveTo(cueBall.x - Math.cos(cueAngle) * ballRadius, cueBall.y - Math.sin(cueAngle) * ballRadius);
        ctx.lineTo(cueEndX, cueEndY);
        ctx.strokeStyle = '#8B4513';
        ctx.lineWidth = ballRadius / 2;
        ctx.stroke();
        ctx.closePath();

        ctx.beginPath();
        ctx.arc(cueEndX, cueEndY, ballRadius / 4, 0, Math.PI * 2);
        ctx.fillStyle = '#FFF';
        ctx.fill();
        ctx.closePath();
    }
}

function checkCollisions() {
    for (let i = 0; i < balls.length; i++) {
        for (let j = i + 1; j < balls.length; j++) {
            const ball1 = balls[i];
            const ball2 = balls[j];

            const dx = ball2.x - ball1.x;
            const dy = ball2.y - ball1.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < ballRadius * 2) {
                const angle = Math.atan2(dy, dx);
                const sin = Math.sin(angle);
                const cos = Math.cos(angle);

                const vx1 = ball1.vx * cos + ball1.vy * sin;
                const vy1 = ball1.vy * cos - ball1.vx * sin;
                const vx2 = ball2.vx * cos + ball2.vy * sin;
                const vy2 = ball2.vy * cos - ball2.vx * sin;

                ball1.vx = vx2 * cos - vy1 * sin;
                ball1.vy = vy1 * cos + vx2 * sin;
                ball2.vx = vx1 * cos - vy2 * sin;
                ball2.vy = vy2 * cos + vx1 * sin;

                const overlap = ballRadius * 2 - distance;
                ball1.x -= overlap / 2 * cos;
                ball1.y -= overlap / 2 * sin;
                ball2.x += overlap / 2 * cos;
                ball2.y += overlap / 2 * sin;
            }
        }
    }
}

function checkPockets() {
    for (let ball of balls) {
        for (let pocket of pockets) {
            const dx = ball.x - pocket.x;
            const dy = ball.y - pocket.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < pocketRadius) {
                if (ball === cueBall) {
                    ball.x = canvasWidth * 0.75;
                    ball.y = canvasHeight / 2;
                    ball.vx = 0;
                    ball.vy = 0;
                    currentPlayer = currentPlayer === 'human' ? 'computer' : 'human';
                } else {
                    ball.pocketed = true;
                    lastPocketedBall = ball;
                    if (!humanType && currentPlayer === 'human') {
                        humanType = ball.number < 8 ? 'solids' : 'stripes';
                        computerType = ball.number < 8 ? 'stripes' : 'solids';
                    }
                    // Add score
                    if (currentPlayer === 'human') {
                        humanScore += 1;
                    } else {
                        computerScore += 1;
                    }
                }
            }
        }
    }
    balls = balls.filter(ball => !ball.pocketed);
}

function update() {
    updatePowerBar();

    if (gameState === 'shooting') {
        balls.forEach(ball => ball.update());
        checkCollisions();
        checkPockets();

        if (balls.every(ball => Math.abs(ball.vx) < 0.05 && Math.abs(ball.vy) < 0.05)) {
            gameState = 'nextTurn';
            setTimeout(() => {
                if (lastPocketedBall) {
                    if (lastPocketedBall.number === 8) {
                        if (currentPlayerAllPocketed()) {
                            alert(currentPlayer === 'human' ? 'شما برنده شدید!' : 'کامپیوتر برنده شد!');
                        } else {
                            alert(currentPlayer === 'human' ? 'شما باختید! توپ 8 را زود انداختید.' : 'کامپیوتر باخت! توپ 8 را زود انداخت.');
                            currentPlayer = currentPlayer === 'human' ? 'computer' : 'human';
                        }
                        resetGame();
                    } else if ((currentPlayer === 'human' && humanType === 'solids' && lastPocketedBall.number > 8) ||
                               (currentPlayer === 'human' && humanType === 'stripes' && lastPocketedBall.number < 8) ||
                               (currentPlayer === 'computer' && computerType === 'solids' && lastPocketedBall.number > 8) ||
                               (currentPlayer === 'computer' && computerType === 'stripes' && lastPocketedBall.number < 8)) {
                        currentPlayer = currentPlayer === 'human' ? 'computer' : 'human';
                    }
                } else {
                    currentPlayer = currentPlayer === 'human' ? 'computer' : 'human';
                }
                lastPocketedBall = null;
                gameState = 'aiming';
                updateScoreBoard();
                if (currentPlayer === 'computer') {
                    setTimeout(computerTurn, 500);
                }
            }, 500);
        }
    }
}

function currentPlayerAllPocketed() {
    const playerType = currentPlayer === 'human' ? humanType : computerType;
    if (playerType === 'solids') {
        return !balls.some(ball => ball.number > 0 && ball.number < 8);
    } else {
        return !balls.some(ball => ball.number > 8);
    }
}

function resetGame() {
    initializeBalls();
    currentPlayer = 'human';
    humanType = null;
    computerType = null;
    lastPocketedBall = null;
    humanScore = 0;
    computerScore = 0;
    gameState = 'aiming';
    updateScoreBoard();
}

function updatePowerBar() {
    if (gameState === 'powerAdjust') {
        cuePower += 1;
        if (cuePower > 20) cuePower = 20;
        powerBar.style.height = (cuePower / 20 * 100) + '%';
    }
}

function updateScoreBoard() {
    let playerType = '';
    if (humanType) {
        playerType = currentPlayer === 'human' ? ` (${humanType === 'solids' ? 'توپ‌های رنگی' : 'توپ‌های راه‌راه'})` : ` (${computerType === 'solids' ? 'توپ‌های رنگی' : 'توپ‌های راه‌راه'})`;
    }
    scoreBoard.innerHTML = `نوبت ${currentPlayer === 'human' ? 'شما' : 'کامپیوتر'}${playerType} | شما (امتیاز: ${humanScore}) | کامپیوتر (امتیاز: ${computerScore})`;
}

function draw() {
    ctx.clearRect(0, 0, canvasWidth, canvasHeight);
    drawTable();
    balls.forEach(ball => ball.draw());
    drawCue();
    
    requestAnimationFrame(draw);
}

function resizeCanvas() {
    const container = document.getElementById('gameContainer');
    const containerWidth = container.clientWidth;
    const containerHeight = container.clientHeight;

    const aspectRatio = 2/1; // Pool table aspect ratio (2:1 for horizontal layout)
    let newWidth, newHeight;

    if (containerWidth / containerHeight > aspectRatio) {
        // Fit to height
        newHeight = Math.min(containerHeight * 0.7, 150); // Reduced max height to 150px
        newWidth = newHeight * aspectRatio;
    } else {
        // Fit to width
        newWidth = Math.min(containerWidth * 0.8, 300);
        newHeight = newWidth / aspectRatio;
    }

    canvas.width = canvasWidth = newWidth;
    canvas.height = canvasHeight = newHeight;

    ballRadius = Math.min(canvasWidth, canvasHeight) * 0.018;
    pocketRadius = ballRadius * 1.7;
    railWidth = ballRadius * 1.8;

    initializeBalls();
    initializePockets();
}

function gameLoop() {
    update();
    draw();
    requestAnimationFrame(gameLoop);
}

function computerTurn() {
    if (currentPlayer !== 'computer') return;

    let targetBalls = balls.filter(ball => 
        (computerType === 'solids' && ball.number > 0 && ball.number < 8) ||
        (computerType === 'stripes' && ball.number > 8) ||
        (currentPlayerAllPocketed() && ball.number === 8)
    );

    if (targetBalls.length === 0) {
        targetBalls = balls.filter(ball => ball !== cueBall);
    }

    const targetBall = targetBalls[Math.floor(Math.random() * targetBalls.length)];
    
    const dx = targetBall.x - cueBall.x;
    const dy = targetBall.y - cueBall.y;
    cueAngle = Math.atan2(dy, dx);

    cueAngle += (Math.random() - 0.5) * 0.2;

    cuePower = 8 + Math.random() * 8;

    setTimeout(() => {
        cueBall.vx = Math.cos(cueAngle) * cuePower * speedMultiplier;
        cueBall.vy = Math.sin(cueAngle) * cuePower * speedMultiplier;
        gameState = 'shooting';
    }, 500);
}

window.addEventListener('resize', resizeCanvas);

// Control button event listeners
startBtn.addEventListener('click', () => {
    if (gameState === 'notStarted') {
        gameState = 'aiming';
        startBtn.textContent = 'شروع مجدد';
    } else {
        resetGame();
    }
});

shootBtn.addEventListener('click', () => {
    if (gameState === 'aiming') {
        gameState = 'powerAdjust';
    } else if (gameState === 'powerAdjust') {
        cueBall.vx = Math.cos(cueAngle) * cuePower * speedMultiplier;
        cueBall.vy = Math.sin(cueAngle) * cuePower * speedMultiplier;
        gameState = 'shooting';
        cuePower = 0;
        powerBar.style.height = '0%';
    }
});

// Arrow control event listeners
const arrowStep = 0.05;

function handleArrowControl(direction) {
    if (gameState === 'aiming' || gameState === 'powerAdjust') {
        switch(direction) {
            case 'up':
                cueAngle -= arrowStep;
                break;
            case 'down':
                cueAngle += arrowStep;
                break;
            case 'left':
                cueAngle += arrowStep;
                break;
            case 'right':
                cueAngle -= arrowStep;
                break;
        }
        cueAngle = (cueAngle + 2 * Math.PI) % (2 * Math.PI);
    }
}

function createArrowHandler(direction) {
    let intervalId = null;
    return {
        start: (event) => {
            event.preventDefault();
            handleArrowControl(direction);
            intervalId = setInterval(() => handleArrowControl(direction), 50);
        },
        stop: () => {
            if (intervalId !== null) {
                clearInterval(intervalId);
                intervalId = null;
            }
        }
    };
}

const arrowHandlers = {
    up: createArrowHandler('up'),
    down: createArrowHandler('down'),
    left: createArrowHandler('left'),
    right: createArrowHandler('right')
};

arrowUp.addEventListener('mousedown', arrowHandlers.up.start);
arrowUp.addEventListener('touchstart', arrowHandlers.up.start);
arrowDown.addEventListener('mousedown', arrowHandlers.down.start);
arrowDown.addEventListener('touchstart', arrowHandlers.down.start);
arrowLeft.addEventListener('mousedown', arrowHandlers.left.start);
arrowLeft.addEventListener('touchstart', arrowHandlers.left.start);
arrowRight.addEventListener('mousedown', arrowHandlers.right.start);
arrowRight.addEventListener('touchstart', arrowHandlers.right.start);

document.addEventListener('mouseup', () => {
    arrowHandlers.up.stop();
    arrowHandlers.down.stop();
    arrowHandlers.left.stop();
    arrowHandlers.right.stop();
});

document.addEventListener('touchend', () => {
    arrowHandlers.up.stop();
    arrowHandlers.down.stop();
    arrowHandlers.left.stop();
    arrowHandlers.right.stop();
});

resizeCanvas();
gameLoop();
</script>
</body></html>
""",height=500)



    with c1:
        with st.expander("بازی جوجه قشمی", expanded=True):
            st.image("jq.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("بازی معروف فلابی بیرد که اسم این بازی جوجه قشمی است")
                st.image("p.png",width=20)

            if st.button("نمایش کد بازی جوجه قشمی"):

                st.code('''
import streamlit as st
import streamlit.components.v1 as components




components.html("""

<html><head><base href="https://websimgames.com/flappy-bird/" target="_blank"><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>بازی فلاپی پرنده</title>
<style>
    body {
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        # background-color: #87CEEB;
        font-family: Arial, sans-serif;
    }
    #gameCanvas {
        border: 2px solid #fff;
        height: 210px;
    }
    #startScreen, #gameOverScreen {
        position: absolute;
        text-align: center;
        font-size: 14px;
        color: #fff;
        text-shadow: 2px 2px 4px #000;
        background-color: rgba(0,0,0,0.5);
        padding: 20px;
        border-radius: 10px;
    }
    #gameOverScreen {
        display: none;
    }
    button {
        font-size: 20px;
        padding: 10px 20px;
        margin-top: 10px;
        cursor: pointer;
    }
</style>
</head>
<body>
<canvas id="gameCanvas" width="288" height="312"></canvas>
<div id="startScreen">
    <p>برای شروع بازی جوجه قشمی کلیک کنید</p>
</div>
<div id="gameOverScreen">
    <p>بازی تمام شد!</p>
    <p>امتیاز شما: <span id="finalScore"></span></p>
    <button id="restartButton">شروع مجدد</button>
</div>

<script>
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const startScreen = document.getElementById('startScreen');
const gameOverScreen = document.getElementById('gameOverScreen');
const finalScoreElement = document.getElementById('finalScore');
const restartButton = document.getElementById('restartButton');

let bird = {
    x: 50,
    y: canvas.height / 2,
    velocity: 0,
    gravity: 0.5,
    lift: -7,
    size: 20
};

let pipes = [];
let score = 0;
let gameLoop;
let gameStarted = false;

// Load bird image
const birdImg = new Image();
birdImg.src = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48cGF0aCBmaWxsPSIjZmZkNzAwIiBkPSJNNDk2IDI1NmMwIDEzNi45LTExMS4xIDI0OC0yNDggMjQ4UzAgMzkyLjkgMCAyNTYgMTExLjEgOCAyNDggOHMyNDggMTExLjEgMjQ4IDI0OHoiLz48cGF0aCBmaWxsPSIjZmZhYTAwIiBkPSJNNDk2IDI1NmMwIDEzNi45LTExMS4xIDI0OC0yNDggMjQ4cy0yNDgtMTExLjEtMjQ4LTI0OEgzMTJsMTg0LTE4NHptLTI0OC0yNDh2MjQ4SDB6Ii8+PHBhdGggZmlsbD0iIzMzMyIgZD0iTTI0OCA1MmMtMTA4LjIgMC0xOTYgODcuOC0xOTYgMTk2czg3LjggMTk2IDE5NiAxOTYgMTk2LTg3LjggMTk2LTE5NlMzNTYuMiA1MiAyNDggNTJ6Ii8+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTMxMiAxOTJjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDggMjEuNS00OCA0OC00OCA0OCAyMS41IDQ4IDQ4eiIvPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik00MTYgMjA4YzAgOC44LTcuMiAxNi0xNiAxNmgtMzJjLTguOCAwLTE2LTcuMi0xNi0xNnM3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2eiIvPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0zODQgMjcyYzAgOC44LTcuMiAxNi0xNiAxNmgtMzJjLTguOCAwLTE2LTcuMi0xNi0xNnM3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2eiIvPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0zNTIgMzM2YzAgOC44LTcuMiAxNi0xNiAxNmgtMzJjLTguOCAwLTE2LTcuMi0xNi0xNnM3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2eiIvPjwvc3ZnPg==';

function drawBird() {
    ctx.save();
    ctx.translate(bird.x, bird.y);
    ctx.rotate(bird.velocity * 0.1);
    ctx.drawImage(birdImg, -bird.size / 2, -bird.size / 2, bird.size, bird.size);
    ctx.restore();
}

function drawPipes() {
    pipes.forEach(pipe => {
        ctx.fillStyle = '#00AA00';
        ctx.fillRect(pipe.x, 0, pipe.width, pipe.top);
        ctx.fillRect(pipe.x, canvas.height - pipe.bottom, pipe.width, pipe.bottom);
    });
}

function drawScore() {
    ctx.fillStyle = '#FFF';
    ctx.font = '24px Arial';
    ctx.fillText(`امتیاز: ${score}`, 10, 30);
}

function updateGame() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    bird.velocity += bird.gravity;
    bird.y += bird.velocity;
    
    if (bird.y + bird.size / 2 > canvas.height) {
        gameOver();
    }
    
    if (pipes.length === 0 || pipes[pipes.length - 1].x < canvas.width - 200) {
        let gap = 150;
        let pipeHeight = Math.floor(Math.random() * (canvas.height - gap - 100)) + 50;
        pipes.push({
            x: canvas.width,
            top: pipeHeight,
            bottom: canvas.height - pipeHeight - gap,
            width: 50,
            counted: false
        });
    }
    
    pipes.forEach(pipe => {
        pipe.x -= 2;
        
        if (pipe.x + pipe.width < 0) {
            pipes.shift();
        }
        
        if (
            bird.x + bird.size / 2 > pipe.x &&
            bird.x - bird.size / 2 < pipe.x + pipe.width &&
            (bird.y - bird.size / 2 < pipe.top || bird.y + bird.size / 2 > canvas.height - pipe.bottom)
        ) {
            gameOver();
        }
        
        if (pipe.x + pipe.width < bird.x && !pipe.counted) {
            score++;
            pipe.counted = true;
        }
    });
    
    drawPipes();
    drawBird();
    drawScore();
    
    if (gameStarted) {
        gameLoop = requestAnimationFrame(updateGame);
    }
}

function gameOver() {
    cancelAnimationFrame(gameLoop);
    gameStarted = false;
    finalScoreElement.textContent = score;
    gameOverScreen.style.display = 'block';
}

function resetGame() {
    bird.y = canvas.height / 2;
    bird.velocity = 0;
    pipes = [];
    score = 0;
    gameOverScreen.style.display = 'none';
    gameStarted = true;
    gameLoop = requestAnimationFrame(updateGame);
}

canvas.addEventListener('click', () => {
    if (gameStarted) {
        bird.velocity = bird.lift;
    }
});

startScreen.addEventListener('click', () => {
    startScreen.style.display = 'none';
    resetGame();
});

restartButton.addEventListener('click', resetGame);

// Initial draw
drawBird();
</script>
</body></html>
""",height=500)
''',language='python')
                

            if st.button("اجرای بازی جوجه قشمی"):


                components.html("""

<html><head><base href="https://websimgames.com/flappy-bird/" target="_blank"><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>بازی فلاپی پرنده</title>
<style>
    body {
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        # background-color: #87CEEB;
        font-family: Arial, sans-serif;
    }
    #gameCanvas {
        border: 2px solid #fff;
        height: 210px;
    }
    #startScreen, #gameOverScreen {
        position: absolute;
        text-align: center;
        font-size: 14px;
        color: #fff;
        text-shadow: 2px 2px 4px #000;
        background-color: rgba(0,0,0,0.5);
        padding: 20px;
        border-radius: 10px;
    }
    #gameOverScreen {
        display: none;
    }
    button {
        font-size: 20px;
        padding: 10px 20px;
        margin-top: 10px;
        cursor: pointer;
    }
</style>
</head>
<body>
<canvas id="gameCanvas" width="288" height="312"></canvas>
<div id="startScreen">
    <p>برای شروع بازی جوجه قشمی کلیک کنید</p>
</div>
<div id="gameOverScreen">
    <p>بازی تمام شد!</p>
    <p>امتیاز شما: <span id="finalScore"></span></p>
    <button id="restartButton">شروع مجدد</button>
</div>

<script>
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const startScreen = document.getElementById('startScreen');
const gameOverScreen = document.getElementById('gameOverScreen');
const finalScoreElement = document.getElementById('finalScore');
const restartButton = document.getElementById('restartButton');

let bird = {
    x: 50,
    y: canvas.height / 2,
    velocity: 0,
    gravity: 0.5,
    lift: -7,
    size: 20
};

let pipes = [];
let score = 0;
let gameLoop;
let gameStarted = false;

// Load bird image
const birdImg = new Image();
birdImg.src = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48cGF0aCBmaWxsPSIjZmZkNzAwIiBkPSJNNDk2IDI1NmMwIDEzNi45LTExMS4xIDI0OC0yNDggMjQ4UzAgMzkyLjkgMCAyNTYgMTExLjEgOCAyNDggOHMyNDggMTExLjEgMjQ4IDI0OHoiLz48cGF0aCBmaWxsPSIjZmZhYTAwIiBkPSJNNDk2IDI1NmMwIDEzNi45LTExMS4xIDI0OC0yNDggMjQ4cy0yNDgtMTExLjEtMjQ4LTI0OEgzMTJsMTg0LTE4NHptLTI0OC0yNDh2MjQ4SDB6Ii8+PHBhdGggZmlsbD0iIzMzMyIgZD0iTTI0OCA1MmMtMTA4LjIgMC0xOTYgODcuOC0xOTYgMTk2czg3LjggMTk2IDE5NiAxOTYgMTk2LTg3LjggMTk2LTE5NlMzNTYuMiA1MiAyNDggNTJ6Ii8+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTMxMiAxOTJjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDggMjEuNS00OCA0OC00OCA0OCAyMS41IDQ4IDQ4eiIvPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik00MTYgMjA4YzAgOC44LTcuMiAxNi0xNiAxNmgtMzJjLTguOCAwLTE2LTcuMi0xNi0xNnM3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2eiIvPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0zODQgMjcyYzAgOC44LTcuMiAxNi0xNiAxNmgtMzJjLTguOCAwLTE2LTcuMi0xNi0xNnM3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2eiIvPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0zNTIgMzM2YzAgOC44LTcuMiAxNi0xNiAxNmgtMzJjLTguOCAwLTE2LTcuMi0xNi0xNnM3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2eiIvPjwvc3ZnPg==';

function drawBird() {
    ctx.save();
    ctx.translate(bird.x, bird.y);
    ctx.rotate(bird.velocity * 0.1);
    ctx.drawImage(birdImg, -bird.size / 2, -bird.size / 2, bird.size, bird.size);
    ctx.restore();
}

function drawPipes() {
    pipes.forEach(pipe => {
        ctx.fillStyle = '#00AA00';
        ctx.fillRect(pipe.x, 0, pipe.width, pipe.top);
        ctx.fillRect(pipe.x, canvas.height - pipe.bottom, pipe.width, pipe.bottom);
    });
}

function drawScore() {
    ctx.fillStyle = '#FFF';
    ctx.font = '24px Arial';
    ctx.fillText(`امتیاز: ${score}`, 10, 30);
}

function updateGame() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    bird.velocity += bird.gravity;
    bird.y += bird.velocity;
    
    if (bird.y + bird.size / 2 > canvas.height) {
        gameOver();
    }
    
    if (pipes.length === 0 || pipes[pipes.length - 1].x < canvas.width - 200) {
        let gap = 150;
        let pipeHeight = Math.floor(Math.random() * (canvas.height - gap - 100)) + 50;
        pipes.push({
            x: canvas.width,
            top: pipeHeight,
            bottom: canvas.height - pipeHeight - gap,
            width: 50,
            counted: false
        });
    }
    
    pipes.forEach(pipe => {
        pipe.x -= 2;
        
        if (pipe.x + pipe.width < 0) {
            pipes.shift();
        }
        
        if (
            bird.x + bird.size / 2 > pipe.x &&
            bird.x - bird.size / 2 < pipe.x + pipe.width &&
            (bird.y - bird.size / 2 < pipe.top || bird.y + bird.size / 2 > canvas.height - pipe.bottom)
        ) {
            gameOver();
        }
        
        if (pipe.x + pipe.width < bird.x && !pipe.counted) {
            score++;
            pipe.counted = true;
        }
    });
    
    drawPipes();
    drawBird();
    drawScore();
    
    if (gameStarted) {
        gameLoop = requestAnimationFrame(updateGame);
    }
}

function gameOver() {
    cancelAnimationFrame(gameLoop);
    gameStarted = false;
    finalScoreElement.textContent = score;
    gameOverScreen.style.display = 'block';
}

function resetGame() {
    bird.y = canvas.height / 2;
    bird.velocity = 0;
    pipes = [];
    score = 0;
    gameOverScreen.style.display = 'none';
    gameStarted = true;
    gameLoop = requestAnimationFrame(updateGame);
}

canvas.addEventListener('click', () => {
    if (gameStarted) {
        bird.velocity = bird.lift;
    }
});

startScreen.addEventListener('click', () => {
    startScreen.style.display = 'none';
    resetGame();
});

restartButton.addEventListener('click', resetGame);

// Initial draw
drawBird();
</script>
</body></html>
""",height=500)










    with c2:
        with st.expander("بازی مار", expanded=True):
            st.image("snake.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("ساخت مار بازی با خوردن دانه مار بزگتر میشه و شما نباید مار به خودش برخورد کنه اگر برخورد کرد بازی میسوزه و مجددا بازی شروع میشه")
                st.image("p.png",width=20)
                st.image("js.png",width=20)
            if st.button("نمایش کد بازی Snake"):

                st.code('''
import streamlit as st
import streamlit.components.v1 as components
components.html("""
                        
<html><head><base href="https://desktop.websim.ai/" />
<title>بازی مار با سیب و مربع</title>
<meta charset="UTF-8">
<style>
    html, body {
        height: 100%;
        margin: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        font-family: 'Tahoma', sans-serif;
    }
    #game-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 300px;
        padding: 10px;
        box-sizing: border-box;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    canvas {
        border: 1px solid #ccc;
        margin-bottom: 10px;
        border-radius: 5px;
    }
    #controls {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 5px;
        width: 100%;
        max-width: 150px; /* Adjust this value to change the overall size of the control pad */
    }
    .control-button {
        width: 100%;
        aspect-ratio: 1 / 1;
        font-size: 14px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
        padding: 0;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .control-button:hover {
        background-color: #45a049;
    }
    .control-button:active {
        background-color: #3e8e41;
    }
    .spacer {
        visibility: hidden;
    }
    #score {
        margin-top: 10px;
        font-size: 18px;
        font-weight: bold;
    }
    #game-over {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        display: none;
    }
    #restart-button {
        margin-top: 10px;
        padding: 10px 20px;
        font-size: 16px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
</style>
</head>
<body>
<div id="game-container">
    <canvas width="280" height="280" id="game"></canvas>
    <div id="controls">
        <div class="spacer"></div>
        <button class="control-button" id="up">↑</button>
        <div class="spacer"></div>
        <button class="control-button" id="left">←</button>
        <div class="spacer"></div>
        <button class="control-button" id="right">→</button>
        <div class="spacer"></div>
        <button class="control-button" id="down">↓</button>
        <div class="spacer"></div>
    </div>
    <div id="score">امتیاز: 0</div>
</div>
<div id="game-over">
    <h2>بازی تمام شد!</h2>
    <p>امتیاز نهایی: <span id="final-score"></span></p>
    <button id="restart-button">شروع مجدد</button>
</div>
<script>
var canvas = document.getElementById('game');
var context = canvas.getContext('2d');
var scoreElement = document.getElementById('score');
var gameOverElement = document.getElementById('game-over');
var finalScoreElement = document.getElementById('final-score');
var restartButton = document.getElementById('restart-button');
var grid = 14;
var count = 0;
var score = 0;
var gameRunning = true;
var snake = {
    x: 140,
    y: 140,
    dx: grid,
    dy: 0,
    cells: [],
    maxCells: 4
};
var apple = {
    x: 280,
    y: 280
};
var square = {
    x: 0,
    y: 0,
    active: false
};
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}
function spawnSquare() {
    square.x = getRandomInt(0, 20) * grid;
    square.y = getRandomInt(0, 20) * grid;
    square.active = true;
}
function resetGame() {
    snake.x = 140;
    snake.y = 140;
    snake.cells = [];
    snake.maxCells = 4;
    snake.dx = grid;
    snake.dy = 0;
    score = 0;
    scoreElement.textContent = 'امتیاز: ' + score;
    apple.x = getRandomInt(0, 20) * grid;
    apple.y = getRandomInt(0, 20) * grid;
    spawnSquare();
    gameOverElement.style.display = 'none';
    gameRunning = true;
}
function gameOver() {
    gameRunning = false;
    finalScoreElement.textContent = score;
    gameOverElement.style.display = 'block';
}
function loop() {
    requestAnimationFrame(loop);
    if (!gameRunning) return;
    if (++count < 4) {
        return;
    }
    count = 0;
    context.clearRect(0, 0, canvas.width, canvas.height);
    snake.x += snake.dx;
    snake.y += snake.dy;
    if (snake.x < 0) {
        snake.x = canvas.width - grid;
    } else if (snake.x >= canvas.width) {
        snake.x = 0;
    }
    if (snake.y < 0) {
        snake.y = canvas.height - grid;
    } else if (snake.y >= canvas.height) {
        snake.y = 0;
    }
    snake.cells.unshift({ x: snake.x, y: snake.y });
    if (snake.cells.length > snake.maxCells) {
        snake.cells.pop();
    }
    context.fillStyle = 'red';
    context.fillRect(apple.x, apple.y, grid - 1, grid - 1);
    if (square.active) {
        context.fillStyle = 'blue';
        context.fillRect(square.x, square.y, grid - 1, grid - 1);
    }
    context.fillStyle = 'green';
    snake.cells.forEach(function (cell, index) {
        context.fillRect(cell.x, cell.y, grid - 1, grid - 1);
        if (cell.x === apple.x && cell.y === apple.y) {
            snake.maxCells++;
            score++;
            scoreElement.textContent = 'امتیاز: ' + score;
            apple.x = getRandomInt(0, 20) * grid;
            apple.y = getRandomInt(0, 20) * grid;
        }
        if (square.active && cell.x === square.x && cell.y === square.y) {
            snake.maxCells += 2;
            score += 2;
            scoreElement.textContent = 'امتیاز: ' + score;
            spawnSquare();
        }
        for (var i = index + 1; i < snake.cells.length; i++) {
            if (cell.x === snake.cells[i].x && cell.y === snake.cells[i].y) {
                gameOver();
                return;
            }
        }
    });
}
function changeDirection(dx, dy) {
    if (gameRunning && dx !== -snake.dx && dy !== -snake.dy) {
        snake.dx = dx;
        snake.dy = dy;
    }
}
document.addEventListener('keydown', function (e) {
    if (e.which === 37) {
        changeDirection(-grid, 0);
    } else if (e.which === 38) {
        changeDirection(0, -grid);
    } else if (e.which === 39) {
        changeDirection(grid, 0);
    } else if (e.which === 40) {
        changeDirection(0, grid);
    }
});
document.getElementById('left').addEventListener('click', function () {
    changeDirection(-grid, 0);
});
document.getElementById('up').addEventListener('click', function () {
    changeDirection(0, -grid);
});
document.getElementById('right').addEventListener('click', function () {
    changeDirection(grid, 0);
});
document.getElementById('down').addEventListener('click', function () {
    changeDirection(0, grid);
});
restartButton.addEventListener('click', resetGame);
spawnSquare();
requestAnimationFrame(loop);
</script>
</body></html>
""",height=700)
    
'''
    

    ,language="javascript")
            
            
            if st.button("اجرا کنید"):



                components.html("""
<html><head><base href="https://desktop.websim.ai/" />
<title>بازی مار با سیب و مربع</title>
<meta charset="UTF-8">
<style>
    html, body {
        height: 100%;
        margin: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        font-family: 'Tahoma', sans-serif;
    }
    #game-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 300px;
        padding: 10px;
        box-sizing: border-box;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    canvas {
        border: 1px solid #ccc;
        margin-bottom: 10px;
        border-radius: 5px;
    }
    #controls {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 5px;
        width: 100%;
        max-width: 150px; /* Adjust this value to change the overall size of the control pad */
    }
    .control-button {
        width: 100%;
        aspect-ratio: 1 / 1;
        font-size: 14px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
        padding: 0;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .control-button:hover {
        background-color: #45a049;
    }
    .control-button:active {
        background-color: #3e8e41;
    }
    .spacer {
        visibility: hidden;
    }
    #score {
        margin-top: 10px;
        font-size: 18px;
        font-weight: bold;
    }
    #game-over {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        display: none;
    }
    #restart-button {
        margin-top: 10px;
        padding: 10px 20px;
        font-size: 16px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
</style>
</head>
<body>
<div id="game-container">
    <canvas width="280" height="280" id="game"></canvas>
    <div id="controls">
        <div class="spacer"></div>
        <button class="control-button" id="up">↑</button>
        <div class="spacer"></div>
        <button class="control-button" id="left">←</button>
        <div class="spacer"></div>
        <button class="control-button" id="right">→</button>
        <div class="spacer"></div>
        <button class="control-button" id="down">↓</button>
        <div class="spacer"></div>
    </div>
    <div id="score">امتیاز: 0</div>
</div>
<div id="game-over">
    <h2>بازی تمام شد!</h2>
    <p>امتیاز نهایی: <span id="final-score"></span></p>
    <button id="restart-button">شروع مجدد</button>
</div>
<script>
var canvas = document.getElementById('game');
var context = canvas.getContext('2d');
var scoreElement = document.getElementById('score');
var gameOverElement = document.getElementById('game-over');
var finalScoreElement = document.getElementById('final-score');
var restartButton = document.getElementById('restart-button');
var grid = 14;
var count = 0;
var score = 0;
var gameRunning = true;
var snake = {
    x: 140,
    y: 140,
    dx: grid,
    dy: 0,
    cells: [],
    maxCells: 4
};
var apple = {
    x: 280,
    y: 280
};
var square = {
    x: 0,
    y: 0,
    active: false
};
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}
function spawnSquare() {
    square.x = getRandomInt(0, 20) * grid;
    square.y = getRandomInt(0, 20) * grid;
    square.active = true;
}
function resetGame() {
    snake.x = 140;
    snake.y = 140;
    snake.cells = [];
    snake.maxCells = 4;
    snake.dx = grid;
    snake.dy = 0;
    score = 0;
    scoreElement.textContent = 'امتیاز: ' + score;
    apple.x = getRandomInt(0, 20) * grid;
    apple.y = getRandomInt(0, 20) * grid;
    spawnSquare();
    gameOverElement.style.display = 'none';
    gameRunning = true;
}
function gameOver() {
    gameRunning = false;
    finalScoreElement.textContent = score;
    gameOverElement.style.display = 'block';
}
function loop() {
    requestAnimationFrame(loop);
    if (!gameRunning) return;
    if (++count < 4) {
        return;
    }
    count = 0;
    context.clearRect(0, 0, canvas.width, canvas.height);
    snake.x += snake.dx;
    snake.y += snake.dy;
    if (snake.x < 0) {
        snake.x = canvas.width - grid;
    } else if (snake.x >= canvas.width) {
        snake.x = 0;
    }
    if (snake.y < 0) {
        snake.y = canvas.height - grid;
    } else if (snake.y >= canvas.height) {
        snake.y = 0;
    }
    snake.cells.unshift({ x: snake.x, y: snake.y });
    if (snake.cells.length > snake.maxCells) {
        snake.cells.pop();
    }
    context.fillStyle = 'red';
    context.fillRect(apple.x, apple.y, grid - 1, grid - 1);
    if (square.active) {
        context.fillStyle = 'blue';
        context.fillRect(square.x, square.y, grid - 1, grid - 1);
    }
    context.fillStyle = 'green';
    snake.cells.forEach(function (cell, index) {
        context.fillRect(cell.x, cell.y, grid - 1, grid - 1);
        if (cell.x === apple.x && cell.y === apple.y) {
            snake.maxCells++;
            score++;
            scoreElement.textContent = 'امتیاز: ' + score;
            apple.x = getRandomInt(0, 20) * grid;
            apple.y = getRandomInt(0, 20) * grid;
        }
        if (square.active && cell.x === square.x && cell.y === square.y) {
            snake.maxCells += 2;
            score += 2;
            scoreElement.textContent = 'امتیاز: ' + score;
            spawnSquare();
        }
        for (var i = index + 1; i < snake.cells.length; i++) {
            if (cell.x === snake.cells[i].x && cell.y === snake.cells[i].y) {
                gameOver();
                return;
            }
        }
    });
}
function changeDirection(dx, dy) {
    if (gameRunning && dx !== -snake.dx && dy !== -snake.dy) {
        snake.dx = dx;
        snake.dy = dy;
    }
}
document.addEventListener('keydown', function (e) {
    if (e.which === 37) {
        changeDirection(-grid, 0);
    } else if (e.which === 38) {
        changeDirection(0, -grid);
    } else if (e.which === 39) {
        changeDirection(grid, 0);
    } else if (e.which === 40) {
        changeDirection(0, grid);
    }
});
document.getElementById('left').addEventListener('click', function () {
    changeDirection(-grid, 0);
});
document.getElementById('up').addEventListener('click', function () {
    changeDirection(0, -grid);
});
document.getElementById('right').addEventListener('click', function () {
    changeDirection(grid, 0);
});
document.getElementById('down').addEventListener('click', function () {
    changeDirection(0, grid);
});
restartButton.addEventListener('click', resetGame);
spawnSquare();
requestAnimationFrame(loop);
</script>
</body></html>
""",height=700)


    with c3:
        with st.expander("بازی تیم دلفین گربدان", expanded=True):
            st.image("gorbedan.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("بازی نبرد توب با تیم دلفین توب باید از بین بازیکنان تیم دلفین رد بشه و اگر به بازیکنان برخورد کرد بازی رو میبازی")
                st.image("p.png",width=20)
            if st.button("نمایش کد بازی تیم دلفین"):

                st.code('''
import streamlit as st
if st.button("بازی تیم دلفین"):
    import pygame
    import pygame.mixer
    import random
    # تنظیمات اولیه
    WINDOW_WIDTH = 450
    WINDOW_HEIGHT = 500
    FPS = 60
    # رنگ‌ها
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    # کلاس پرنده
    class Bird(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load("ball.png")
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.velocity = 0
            self.gravity = 0.5
        def update(self):
            self.velocity += self.gravity
            self.rect.y += self.velocity
            if self.rect.top <= 0:
                self.rect.top = 0
                self.velocity = 0
            if self.rect.bottom >= WINDOW_HEIGHT:
                self.rect.bottom = WINDOW_HEIGHT
                self.velocity = 0
        def flap(self):
            self.velocity = -10
    # کلاس لوله
    class Pipe(pygame.sprite.Sprite):
        pipe_images = ["a0.png", "a1.png", "a2.png", "a3.png", "a4.png", 
                    "a5.png", "a6.png", "a7.png", "a8.png", "a9.png", 
                    "a10.png", "a11.png", "a12.png", "a13.png", "a14.png", 
                    "a15.png", "a16.png", "a17.png", "a18.png", "a19.png", 
                    "a20.png"]
        def __init__(self, x, y, is_top):
            super().__init__()
            self.image = pygame.image.load(random.choice(self.pipe_images))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y if not is_top else y - self.rect.height
            self.is_top = is_top
            self.speed = 2
        def update(self):
            self.rect.x -= self.speed
            if self.rect.right < 0:
                self.kill()
    # تابع راه‌اندازی مجدد بازی
    def restart_game():
        global bird, all_sprites, pipes, score, last_score
        pygame.mixer.music.stop()  # قطع موسیقی در هنگام ریستارت
        bird = Bird(100, WINDOW_HEIGHT // 2)
        all_sprites.empty()
        pipes.empty()
        all_sprites.add(bird)
        score = 0
        last_score = 0  # تنظیم امتیاز آخر به 0
    # تابع اصلی
    def main():
        pygame.init()
        pygame.mixer.init()  # بارگذاری کتابخانه صدا
        # بارگذاری و پخش موسیقی پس‌زمینه
        pygame.mixer.music.load("toop.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # پخش موسیقی به صورت تکراری
        # بارگذاری صداها
        score_sounds = [
            pygame.mixer.Sound("a0.mp3"),
            pygame.mixer.Sound("a1.mp3"),
            pygame.mixer.Sound("a2.mp3"),
            pygame.mixer.Sound("a6.mp3"),
        ]
        crash_sounds = [
            pygame.mixer.Sound("a4.mp3"),
        ]
        for sound in score_sounds:
            sound.set_volume(0.5)  # تنظیم میزان صدا
        for sound in crash_sounds:
            sound.set_volume(0.5)  # تنظیم میزان صدا
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("دلفین گربدان")
        clock = pygame.time.Clock()
        # تصویر پس‌زمینه
        background = pygame.image.load("bac.jpg").convert()
        # گروه اشیاء شامل پرنده و لوله‌ها
        global all_sprites, pipes, score, last_score
        all_sprites = pygame.sprite.Group()
        pipes = pygame.sprite.Group()
        # ایجاد پرنده
        global bird
        bird = Bird(100, WINDOW_HEIGHT // 2)
        all_sprites.add(bird)
        # فاصله زمانی بین ایجاد لوله‌ها
        pipe_timer = 0
        pipe_interval = 1.5 * FPS
        game_over = False
        game_start = False
        restart_button = pygame.Rect(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 + 50, 100, 50)
        play_button = pygame.Rect(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 - 25, 100, 50)
        font_path = pygame.font.match_font('Arial')
        font = pygame.font.Font(font_path, 36)
        small_font = pygame.font.Font(font_path, 24)
        score = 0
        last_score = 0  # متغیر جدید برای ذخیره امتیاز در زمان باخت
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and not game_over and game_start:
                    bird.flap()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and game_over:
                        restart_game()
                        game_over = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.collidepoint(event.pos) and game_over:
                        restart_game()
                        game_over = False
                    if play_button.collidepoint(event.pos) and not game_start:
                        restart_game()
                        game_start = True
            if game_start:
                if not game_over:
                    # ایجاد لوله‌های جدید
                    pipe_timer += 1
                    if pipe_timer >= pipe_interval:
                        pipe_timer = 0
                        pipe_height = random.randint(100, WINDOW_HEIGHT - 200)
                        top_pipe = Pipe(WINDOW_WIDTH, pipe_height, True)
                        bottom_pipe = Pipe(WINDOW_WIDTH, pipe_height + 150, False)
                        pipes.add(top_pipe)
                        pipes.add(bottom_pipe)
                    # به‌روزرسانی اشیاء
                    all_sprites.update()
                    pipes.update()
                    # بررسی برخورد
                    if pygame.sprite.spritecollide(bird, pipes, False) or bird.rect.top <= 0 or bird.rect.bottom >= WINDOW_HEIGHT:
                        last_score = score  # ذخیره امتیاز در زمان باخت
                        game_over = True
                        pygame.mixer.music.stop()  # قطع موسیقی در هنگام باخت
                        random_crash_sound = random.choice(crash_sounds)
                        random_crash_sound.play()  # پخش صدای سقوط
                    # بررسی عبور پرنده از لوله‌ها
                    for pipe in pipes:
                        if pipe.rect.right < bird.rect.left and not hasattr(pipe, 'passed'):
                            pipe.passed = True
                            if not pipe.is_top:
                                score += 2
                                random_sound = random.choice(score_sounds)
                                pygame.mixer.stop()  # قطع صدای فعلی
                                random_sound.play()  # پخش صدای تصادفی
                    # نمایش صفحه
                    screen.blit(background, (0, 0))  # نمایش پس‌زمینه
                    all_sprites.draw(screen)
                    pipes.draw(screen)
                    # نمایش امتیاز
                    score_text = font.render(f"Soccer: {score}", True, WHITE)
                    screen.blit(score_text, (10, 10))
                    small_image = pygame.image.load("logo.png")
                    small_image = pygame.transform.scale(small_image, (40, 40))
                    screen.blit(small_image, (370, 10))
                else:
                    # منوی پایان بازی
                    screen.blit(background, (0, 0))  # نمایش پس‌زمینه
                    small_image = pygame.image.load("logo.png")
                    small_image = pygame.transform.scale(small_image, (130, 130))
                    screen.blit(small_image, (160, 40))
                    small_image = pygame.image.load("a0.png")
                    small_image = pygame.transform.scale(small_image, (50, 50))
                    screen.blit(small_image, (200, 430))
                    restart_text = small_font.render("Restart", True, BLACK)
                    pygame.draw.rect(screen, WHITE, restart_button)
                    screen.blit(restart_text, (restart_button.x + (restart_button.width // 2 - restart_text.get_width() // 2),
                                            restart_button.y + (restart_button.height // 2 - restart_text.get_height() // 2)))
                    # نمایش امتیاز آخر
                    score_text = small_font.render(f"Last Score: {last_score}", True, BLACK)
                    screen.blit(score_text, (WINDOW_WIDTH // 2 - score_text.get_width() // 2, restart_button.y - 30))
            else:
                # صفحه شروع بازی
                screen.blit(background, (0, 0))  # نمایش پس‌زمینه
                pygame.draw.rect(screen, WHITE, play_button)
                imglogo = pygame.image.load("logo.png")
                imglogo = pygame.transform.scale(imglogo, (140, 140))
                screen.blit(imglogo, (160, 50))
                small_image = pygame.image.load("a0.png")
                small_image = pygame.transform.scale(small_image, (50, 50))
                screen.blit(small_image, (200, 430))
                play_text = small_font.render("Play", True, BLACK)
                screen.blit(play_text, (play_button.x + (play_button.width // 2 - play_text.get_width() // 2),
                                        play_button.y + (play_button.height // 2 - play_text.get_height() // 2)))
            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()
    if __name__ == "__main__":
        main()
''')
            st.warning("برای اجرای بازی به محیط برنامه نویسی نیاز دارید")



if menu_id == "ساخت برنامه":

    st.divider()

    col1,col3 = st.columns(2)


    with col1:
        with st.expander("✨ فوتو قشمی", expanded=True):
            st.image("photo.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("برنامه ویرایش عکس که میتونید فایل مورد نظر رو آپلود کنید و عرض و ارتفاع آن را مشخص کنید و فایل ویرایش شده رو دانلود کنید")
            with col2:
                st.image("p.png",width=20)

            if st.button("نمایش کد برنامه فوتو قشمی"):

                st.code('''
    import streamlit as st
    from PIL import Image
    import base64
    from io import BytesIO
    def main():
        # بارگذاری تصویر
        uploaded_image = st.file_uploader("تصویر را انتخاب کنید", type=["jpg", "jpeg", "png"])
        if uploaded_image is not None:
            # باز کردن تصویر با استفاده از PIL
            image = Image.open(uploaded_image)
            # نمایش تصویر قبل از بزرگنمایی
            st.subheader("تصویر قبل از بزرگنمایی")
            st.image(image, use_column_width=True)
            # بزرگنمایی تصویر
            width = st.slider("عرض تصویر (پیکسل)", 100, 2000, 500)
            height = st.slider("ارتفاع تصویر (پیکسل)", 100, 2000, 500)
            resized_image = image.resize((width, height))
            # نمایش تصویر بعد از بزرگنمایی
            st.subheader("تصویر بعد از بزرگنمایی")
            st.image(resized_image, use_column_width=True)
            # دکمه دانلود تصویر بزرگنمایی شده
            download_button(resized_image)
    def download_button(image):
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        href = f'<a href="data:file/png;base64,{img_str}" download="resized_image.png">دانلود تصویر ویرایش شده</a>'
        st.markdown(href, unsafe_allow_html=True)
    if __name__ == "__main__":
        main()
    st.success("ساخته شده توسط عبدالله چلاسی")
    ''',language="python")
            
            st.success("🔻 فوتو قشمی 🔻")

                

            def main():

                    # بارگذاری تصویر
                uploaded_image = st.file_uploader("تصویر را انتخاب کنید", type=["jpg", "jpeg", "png"])

                if uploaded_image is not None:
                        # باز کردن تصویر با استفاده از PIL
                    image = Image.open(uploaded_image)

                        # نمایش تصویر قبل از بزرگنمایی
                    st.subheader("تصویر قبل از بزرگنمایی")
                    st.image(image, use_column_width=True)

                        # بزرگنمایی تصویر
                    width = st.slider("عرض تصویر (پیکسل)", 100, 2000, 500)
                    height = st.slider("ارتفاع تصویر (پیکسل)", 100, 2000, 500)
                    resized_image = image.resize((width, height))

                        # نمایش تصویر بعد از بزرگنمایی
                    st.subheader("تصویر بعد از بزرگنمایی")
                    st.image(resized_image, use_column_width=True)

                        # دکمه دانلود تصویر بزرگنمایی شده
                    download_button(resized_image)

            def download_button(image):
                buffered = BytesIO()
                image.save(buffered, format="PNG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                href = f'<a href="data:file/png;base64,{img_str}" download="resized_image.png">دانلود تصویر ویرایش شده</a>'
                st.markdown(href, unsafe_allow_html=True)

            if __name__ == "__main__":
                    main()

                    

                
                
    with col3:
        with st.expander("برنامه واتساپ", expanded=True):
            st.image("wa.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("آموزش ساخت چت واتساپ")
                st.image("p.png",width=20)

            if st.button("نمایش کد برنامه واتساپ"):

                st.code('''
import streamlit.components.v1 as components


components.html("""
<html><head><base href="https://whatsapp-clone.example.com/" target="_self">
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>واتساپ کلون</title>
<style>
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    direction: rtl;
    # background-color: #f0f0f0;
  }
  .container {
    max-width: 500px;
    margin: 0 auto;
    background-color: #fff;
    height: 60vh;
    display: flex;
    flex-direction: column;
  }
  .header {
    background-color: #075e54;
    color: white;
    padding: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .header h2 {
    margin: 0;
  }
  .header-icons {
    display: flex;
    gap: 15px;
  }
  .header-icon {
    cursor: pointer;
    font-size: 18px;
  }
  .content {
    flex: 1;
    overflow-y: auto;
  }
  .chat-list, .chat-window, .status-page, .calls-page, .contacts-page, .settings-page {
    height: 100%;
    overflow-y: auto;
  }
  .chat-item, .setting-item, .status-item, .call-item, .contact-item {
    padding: 10px;
    border-bottom: 1px solid #ddd;
    cursor: pointer;
    display: flex;
    align-items: center;
  }
  .chat-item:hover, .setting-item:hover, .status-item:hover, .call-item:hover, .contact-item:hover {
    background-color: #f5f5f5;
  }
  .message-input {
    display: flex;
    padding-left: 40px;
    background-color: #f0f0f0;
  }
  .message-input input {
    flex: 1;
    padding: 10px;
    border: none;
    border-radius: 20px;
  }
  .message-input button {
    background-color: #075e54;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 50%;
    margin-right: 10px;
    cursor: pointer;
  }
  .message {
    max-width: 70%;
    margin: 10px;
    padding: 10px;
    border-radius: 10px;
  }
  .sent {
    background-color: #dcf8c6;
    align-self: flex-end;
  }
  .received {
    background-color: #fff;
    align-self: flex-start;
  }
  .back-button {
    background-color: transparent;
    border: none;
    color: white;
    font-size: 18px;
    cursor: pointer;
  }
  .bottom-nav {
    display: flex;
    justify-content: space-around;
    background-color: #f0f0f0;
    padding: 10px 0;
  }
  .nav-item {
    text-align: center;
    cursor: pointer;
  }
  .nav-item i {
    font-size: 24px;
    color: #075e54;
  }
  .nav-item.active i {
    color: #128c7e;
  }
  .dropdown {
    position: relative;
    display: inline-block;
  }
  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
    left: 0;
  }
  .dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
  }
  .dropdown-content a:hover {
    background-color: #f1f1f1;
  }
  .show {
    display: block;
  }
  .avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background-color: #128c7e;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    font-size: 24px;
    margin-left: 10px;
  }
  .contact-info, .call-info {
    flex: 1;
  }
  .call-icon {
    margin-right: 10px;
    color: #075e54;
  }
  .keyboard {
    display: none;
    background-color: #f0f0f0;
    padding: 0px;
  }
  .keyboard-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 5px;
  }
  .key {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 10px;
    width: 30px;
    text-align: center;
    cursor: pointer;
  }
  .key:hover {
    background-color: #e0e0e0;
  }
  .space-key {
    width: 150px;
  }
  .backspace-key {
    width: 60px;
  }
</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>
  <div class="container" id="app">
    <div class="header">
      <h2 id="page-title">واتساپ</h2>
      <div class="header-icons">
        <i class="fas fa-search header-icon" onclick="showSearch()"></i>
        <div class="dropdown">
          <i class="fas fa-ellipsis-v header-icon" onclick="toggleDropdown()"></i>
          <div id="myDropdown" class="dropdown-content">
            <a onclick="showPage('new-group')">گروه جدید</a>
            <a onclick="showPage('new-broadcast')">پخش جدید</a>
            <a onclick="showPage('linked-devices')">دستگاه‌های متصل</a>
            <a  onclick="showPage('starred-messages')">پیام‌های ستاره‌دار</a>
            <a onclick="showPage('settings')">تنظیمات</a>
          </div>
        </div>
      </div>
    </div>
    
    <div class="content" id="content">
      <div id="chats-page">
        <div class="chat-list" id="chat-list"></div>
      </div>

      <div id="status-page" style="display: none;">
        <h3>وضعیت من</h3>
        <div class="status-item" onclick="updateStatus()">
          <div class="avatar">
            <i class="fas fa-plus"></i>
          </div>
          <div class="status-info">
            <h4>وضعیت من</h4>
            <p>برای به‌روزرسانی وضعیت کلیک کنید</p>
          </div>
        </div>
        <h3>به‌روزرسانی‌های اخیر</h3>
        <div id="status-list"></div>
      </div>

      <div id="calls-page" style="display: none;">
        <h3>تماس‌ها</h3>
        <div id="calls-list"></div>
      </div>

      <div id="contacts-page" style="display: none;">
        <h3>مخاطبان</h3>
        <div id="contacts-list"></div>
      </div>

      <div id="chat-page" style="display: none;">
        <div class="chat-window" id="chat-window"></div>
        <div class="message-input">
          <input type="text" id="message-input" placeholder="پیام خود را بنویسید..." readonly onclick="toggleKeyboard()">
          <button onclick="sendMessage()">ارسال</button>
        </div>
        <div class="keyboard" id="custom-keyboard">
          <div class="keyboard-row">
            <div class="key" onclick="addToInput('ض')">ض</div>
            <div class="key" onclick="addToInput('ص')">ص</div>
            <div class="key" onclick="addToInput('ث')">ث</div>
            <div class="key" onclick="addToInput('ق')">ق</div>
            <div class="key" onclick="addToInput('ف')">ف</div>
            <div class="key" onclick="addToInput('غ')">غ</div>
            <div class="key" onclick="addToInput('ع')">ع</div>
            <div class="key" onclick="addToInput('ه')">ه</div>
            <div class="key" onclick="addToInput('خ')">خ</div>
            <div class="key" onclick="addToInput('ح')">ح</div>
          </div>
          <div class="keyboard-row">
            <div class="key" onclick="addToInput('ش')">ش</div>
            <div class="key" onclick="addToInput('س')">س</div>
            <div class="key" onclick="addToInput('ی')">ی</div>
            <div class="key" onclick="addToInput('ب')">ب</div>
            <div class="key" onclick="addToInput('ل')">ل</div>
            <div class="key" onclick="addToInput('ا')">ا</div>
            <div class="key" onclick="addToInput('ت')">ت</div>
            <div class="key" onclick="addToInput('ن')">ن</div>
            <div class="key" onclick="addToInput('م')">م</div>
            <div class="key" onclick="addToInput('ک')">ک</div>
          </div>
          <div class="keyboard-row">
            <div class="key" onclick="addToInput('ظ')">ظ</div>
            <div class="key" onclick="addToInput('ط')">ط</div>
            <div class="key" onclick="addToInput('ز')">ز</div>
            <div class="key" onclick="addToInput('ر')">ر</div>
            <div class="key" onclick="addToInput('ذ')">ذ</div>
            <div class="key" onclick="addToInput('د')">د</div>
            <div class="key" onclick="addToInput('پ')">پ</div>
            <div class="key" onclick="addToInput('و')">و</div>
            <div class="key" onclick="addToInput('گ')">گ</div>
            <div class="key backspace-key" onclick="backspace()"><i class="fas fa-backspace"></i></div>
          </div>
          <div class="keyboard-row">
            <div class="key" onclick="addToInput('؟')">؟</div>
            <div class="key" onclick="addToInput('!')">!</div>
            <div class="key space-key" onclick="addToInput(' ')">فاصله</div>
            <div class="key" onclick="addToInput('،')">،</div>
            <div class="key" onclick="addToInput('.')">.</div>
          </div>
        </div>
      </div>

      <div id="settings-page" style="display: none;">
        <h3>تنظیمات</h3>
        <div class="setting-item" onclick="showPage('account')">
          <i class="fas fa-user"></i> حساب کاربری
        </div>
        <div class="setting-item" onclick="showPage('privacy')">
          <i class="fas fa-lock"></i> حریم خصوصی
        </div>
        <div class="setting-item" onclick="showPage('chats-settings')">
          <i class="fas fa-comments"></i> تنظیمات چت
        </div>
        <div class="setting-item" onclick="showPage('notifications')">
          <i class="fas fa-bell"></i> اعلان‌ها
        </div>
        <div class="setting-item" onclick="showPage('storage')">
          <i class="fas fa-database"></i> ذخیره‌سازی و داده‌ها
        </div>
        <div class="setting-item" onclick="showPage('help')">
          <i class="fas fa-question-circle"></i> راهنما
        </div>
      </div>

      <div id="new-group-page" style="display: none;">
        <h3>ایجاد گروه جدید</h3>
        <p>اینجا می‌توانید گروه جدید ایجاد کنید.</p>
      </div>

      <div id="new-broadcast-page" style="display: none;">
        <h3>ایجاد پخش جدید</h3>
        <p>اینجا می‌توانید پخش جدید ایجاد کنید.</p>
      </div>

      <div id="linked-devices-page" style="display: none;">
        <h3>دستگاه‌های متصل</h3>
        <p>لیست دستگاه‌های متصل به حساب شما اینجا نمایش داده می‌شود.</p>
      </div>

      <div id="starred-messages-page" style="display: none;">
        <h3>پیام‌های ستاره‌دار</h3>
        <p>پیام‌های ستاره‌دار شما اینجا نمایش داده می‌شود.</p>
      </div>

      <div id="account-page" style="display: none;">
        <h3>تنظیمات حساب کاربری</h3>
        <p>اینجا می‌توانید تنظیمات حساب کاربری خود را تغییر دهید.</p>
      </div>

      <div id="privacy-page" style="display: none;">
        <h3>تنظیمات حریم خصوصی</h3>
        <p>اینجا می‌توانید تنظیمات حریم خصوصی خود را تغییر دهید.</p>
      </div>

      <div id="chats-settings-page" style="display: none;">
        <h3>تنظیمات چت</h3>
        <p>اینجا می‌توانید تنظیمات چت خود را تغییر دهید.</p>
      </div>

      <div id="notifications-page" style="display: none;">
        <h3>تنظیمات اعلان‌ها</h3>
        <p>اینجا می‌توانید تنظیمات اعلان‌های خود را تغییر دهید.</p>
      </div>

      <div id="storage-page" style="display: none;">
        <h3>تنظیمات ذخیره‌سازی و داده‌ها</h3>
        <p>اینجا می‌توانید تنظیمات ذخیره‌سازی و داده‌های خود را مدیریت کنید.</p>
      </div>

      <div id="help-page" style="display: none;">
        <h3>راهنما</h3>
        <p>اینجا می‌توانید اطلاعات راهنما و پشتیبانی را مشاهده کنید.</p>
      </div>
    </div>

    <div class="bottom-nav">
      <div class="nav-item active" onclick="showPage('chats')">
        <i class="fas fa-comments"></i>
        <div>چت‌ها</div>
      </div>
      <div class="nav-item" onclick="showPage('status')">
        <i class="fas fa-circle"></i>
        <div>وضعیت</div>
      </div>
      <div class="nav-item" onclick="showPage('calls')">
        <i class="fas fa-phone"></i>
        <div>تماس‌ها</div>
      </div>
      <div class="nav-item" onclick="showPage('contacts')">
        <i class="fas fa-address-book"></i>
        <div>مخاطبان</div>
      </div>
    </div>
  </div>

  <script>
    const chatList = [
      { id: 1, name: "عبدالله چلاسی", lastMessage: "سلام، چطوری؟" },
      { id: 2, name: "دلفین گربدان", lastMessage: "فردا جلسه داریم" },
      { id: 3, name: "باشگاه قشم", lastMessage: "عکس‌ها رو فرستادم" }
    ];

    const chats = {
      1: [
        { sender: "عبدالله چلاسی", message: "سلام، چطوری؟" },
        { sender: "من", message: "سلام عبدالله چلاسی خوبم ممنون. تو چطوری؟" }
      ],
      2: [
        { sender: "ماجد", message: "فردا جلسه داریم" },
        { sender: "من", message: "باشه، ساعت چند؟" }
      ],
      3: [
        { sender: "عبدالقادر", message: "عکس‌ها رو فرستادم" },
        { sender: "من", message: "دستت درد نکنه، الان میبینم" }
      ]
    };

    const statusList = [
      { id: 1, name: "عبدالله چلاسی", time: "امروز 10:30", content: "در حال مطالعه 📚" },
      { id: 2, name: "محمد", time: "امروز 09:15", content: "سفر به شمال 🌳" },
      { id: 3, name: "فرشاد", time: "دیروز 23:45", content: "شب بخیر دوستان 🌙" }
    ];

    const callsList = [
      { id: 1, name: "عبدالله چلاسی", time: "امروز 14:20", type: "incoming" },
      { id: 2, name: "باشگاه قشم", time: "دیروز 18:45", type: "outgoing" },
      { id: 3, name: "دلفین گربدان", time: "2 روز پیش", type: "missed" },
      { id: 4, name: "قشم", time: "3 روز پیش", type: "incoming" },
      { id: 5, name: "عبدالقادر", time: "هفته پیش", type: "outgoing" }
    ];

    const contactsList = [
      { id: 1, name: "عبدالله چلاسی" },
      { id: 2, name: "عبدالقادر" },
      { id: 3, name: "وحید" },
      { id: 4, name: "عبدالعزیز" },
      { id: 5, name: "ماجد" },
      { id: 6, name: "امیر" },
      { id: 7, name: "فرشاد" },
      { id: 8, name: "یعقوب" },
      { id: 9, name: "ایوب" },
      { id: 10, name: "محمد" }
    ];

    function renderChatList() {
      const chatListElement = document.getElementById("chat-list");
      chatListElement.innerHTML = chatList.map(chat => `
        <div class="chat-item" onclick="openChat(${chat.id}, '${chat.name}')">
          <div class="avatar">${chat.name[0]}</div>
          <div class="contact-info">
            <h3>${chat.name}</h3>
            <p>${chat.lastMessage}</p>
          </div>
        </div>
      `).join("");
    }

    function renderStatusList() {
      const statusListElement = document.getElementById("status-list");
      statusListElement.innerHTML = statusList.map(status => `
        <div class="status-item" onclick="viewStatus(${status.id})">
          <div class="avatar">
            ${status.name[0]}
          </div>
          <div class="status-info">
            <h4>${status.name}</h4>
            <p>${status.time}</p>
          </div>
        </div>
      `).join("");
    }

    function renderCallsList() {
      const callsListElement = document.getElementById("calls-list");
      callsListElement.innerHTML = callsList.map(call => `
        <div class="call-item">
          <div class="avatar">${call.name[0]}</div>
          <div class="call-info">
            <h3>${call.name}</h3>
            <p>${call.time}</p>
          </div>
          <div class="call-icon">
            <i class="fas fa-phone${call.type === 'incoming' ? '-alt' : call.type === 'outgoing' ? '' : '-slash'}" style="color: ${call.type === 'missed' ? 'red' : '#075e54'}"></i>
          </div>
        </div>
      `).join("");
    }

    function renderContactsList() {
      const contactsListElement = document.getElementById("contacts-list");
      contactsListElement.innerHTML = contactsList.map(contact => `
        <div class="contact-item" onclick="openChat(${contact.id}, '${contact.name}')">
          <div class="avatar">${contact.name[0]}</div>
          <div class="contact-info">
            <h3>${contact.name}</h3>
          </div>
        </div>
      `).join("");
    }

    function openChat(chatId, chatName) {
      showPage('chat');
      document.getElementById("page-title").textContent = chatName;
      renderChat(chatId);
    }

    function renderChat(chatId) {
      const chatWindow = document.getElementById("chat-window");
      chatWindow.innerHTML = chats[chatId].map(message => `
        <div class="message ${message.sender === 'من' ? 'sent' : 'received'}">
          <p>${message.message}</p>
        </div>
      `).join("");
      chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    function showPage(pageId) {
      const pages = ['chats', 'status', 'calls', 'contacts', 'chat', 'settings', 'new-group', 'new-broadcast', 'linked-devices', 'starred-messages', 'account', 'privacy', 'chats-settings', 'notifications', 'storage', 'help'];
      pages.forEach(page => {
        document.getElementById(`${page}-page`).style.display = page === pageId ? 'block' : 'none';
      });

      if (pageId !== 'chat') {
        document.getElementById("page-title").textContent = getPageTitle(pageId);
      }

      document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
      });
      if (['chats', 'status', 'calls', 'contacts'].includes(pageId)) {
        document.querySelector(`.nav-item[onclick="showPage('${pageId}')"]`).classList.add('active');
      }

      if (pageId === 'status') {
        renderStatusList();
      } else if (pageId === 'calls') {
        renderCallsList();
      } else if (pageId === 'contacts') {
        renderContactsList();
      }
    }

    function getPageTitle(pageId) {
      const titles = {
        'chats': 'واتساپ',
        'status': 'وضعیت',
        'calls': 'تماس‌ها',
        'contacts': 'مخاطبان',
        'settings': 'تنظیمات',
        'new-group': 'گروه جدید',
        'new-broadcast': 'پخش جدید',
        'linked-devices': 'دستگاه‌های متصل',
        'starred-messages': 'پیام‌های ستاره‌دار',
        'account': 'حساب کاربری',
        'privacy': 'حریم خصوصی',
        'chats-settings': 'تنظیمات چت',
        'notifications': 'اعلان‌ها',
        'storage': 'ذخیره‌سازی و داده‌ها',
        'help': 'راهنما'
      };
      return titles[pageId] || 'واتساپ';
    }

    function sendMessage() {
      const input = document.getElementById("message-input");
      const message = input.value.trim();
      if (message) {
        const chatTitle = document.getElementById("page-title").textContent;
        const chatId = chatList.find(chat => chat.name === chatTitle).id;
        chats[chatId].push({ sender: "من", message: message });
        renderChat(chatId);
        input.value = "";
        
        setTimeout(() => {
          const responses = [
            "فروشگاه دیجی کد عالیه ؟",
            "من عبدالله چلاسی هستم",
            "لطفا فروشگاه دیجی کد رو به بقیه معرفی کنید",
            "به روز ترین فروشگاه دیجی کد که میتونید هم از برنامه استفاده کنید و هم کدهای برنامه رو میتونید مشاهده کنید",
            "لطفا نظرات خودتان را برام ارسال کنید",
            "چطوری رفیق",
            "ممنونم از اینکه فروشگاه دیجی کد رو دانلود کردی",
            "از فروشگاه دیجی کد راضی هستید",
            "سعی میکنم برنامه و بازی های بیشتری توی دیجی کد قرار بدم",
            "اگر وبسایتی یا ابلیکیشنی خواستی با این شماره تماس بگیر 09335825325"
          ];
          const replyMessage = responses[Math.floor(Math.random() * responses.length)];
          chats[chatId].push({ sender: chatTitle, message: replyMessage });
          renderChat(chatId);
        }, 1000 + Math.random() * 2000);
      }
    }

    function toggleDropdown() {
      document.getElementById("myDropdown").classList.toggle("show");
    }

    function showSearch() {
      alert("جستجو");
    }

    function updateStatus() {
      const newStatus = prompt("وضعیت جدید خود را وارد کنید:");
      if (newStatus) {
        alert(`وضعیت شما به '${newStatus}' تغییر کرد.`);
      }
    }

    function viewStatus(statusId) {
      const status = statusList.find(s => s.id === statusId);
      if (status) {
        alert(`نمایش وضعیت ${status.name}: ${status.content}`);
      }
    }

    function toggleKeyboard() {
      const keyboard = document.getElementById('custom-keyboard');
      keyboard.style.display = keyboard.style.display === 'none' ? 'block' : 'none';
    }

    function addToInput(char) {
      const input = document.getElementById('message-input');
      input.value += char;
    }

    function backspace() {
      const input = document.getElementById('message-input');
      input.value = input.value.slice(0, -1);
    }

    window.onclick = function(event) {
      if (!event.target.matches('.header-icon')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
          }
        }
      }
    }

    renderChatList();
    showPage('chats');
  </script>
</body>
</html>
""",height=850)




''')
                
            if st.button("اجرای برنامه واتساپ"):


                components.html("""
<html><head><base href="https://whatsapp-clone.example.com/" target="_self">
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>واتساپ کلون</title>
<style>
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    direction: rtl;
    # background-color: #f0f0f0;
  }
  .container {
    max-width: 500px;
    margin: 0 auto;
    background-color: #fff;
    height: 60vh;
    display: flex;
    flex-direction: column;
  }
  .header {
    background-color: #075e54;
    color: white;
    padding: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .header h2 {
    margin: 0;
  }
  .header-icons {
    display: flex;
    gap: 15px;
  }
  .header-icon {
    cursor: pointer;
    font-size: 18px;
  }
  .content {
    flex: 1;
    overflow-y: auto;
  }
  .chat-list, .chat-window, .status-page, .calls-page, .contacts-page, .settings-page {
    height: 100%;
    overflow-y: auto;
  }
  .chat-item, .setting-item, .status-item, .call-item, .contact-item {
    padding: 10px;
    border-bottom: 1px solid #ddd;
    cursor: pointer;
    display: flex;
    align-items: center;
  }
  .chat-item:hover, .setting-item:hover, .status-item:hover, .call-item:hover, .contact-item:hover {
    background-color: #f5f5f5;
  }
  .message-input {
    display: flex;
    padding-left: 40px;
    background-color: #f0f0f0;
  }
  .message-input input {
    flex: 1;
    padding: 10px;
    border: none;
    border-radius: 20px;
  }
  .message-input button {
    background-color: #075e54;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 50%;
    margin-right: 10px;
    cursor: pointer;
  }
  .message {
    max-width: 70%;
    margin: 10px;
    padding: 10px;
    border-radius: 10px;
  }
  .sent {
    background-color: #dcf8c6;
    align-self: flex-end;
  }
  .received {
    background-color: #fff;
    align-self: flex-start;
  }
  .back-button {
    background-color: transparent;
    border: none;
    color: white;
    font-size: 18px;
    cursor: pointer;
  }
  .bottom-nav {
    display: flex;
    justify-content: space-around;
    background-color: #f0f0f0;
    padding: 10px 0;
  }
  .nav-item {
    text-align: center;
    cursor: pointer;
  }
  .nav-item i {
    font-size: 24px;
    color: #075e54;
  }
  .nav-item.active i {
    color: #128c7e;
  }
  .dropdown {
    position: relative;
    display: inline-block;
  }
  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
    left: 0;
  }
  .dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
  }
  .dropdown-content a:hover {
    background-color: #f1f1f1;
  }
  .show {
    display: block;
  }
  .avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background-color: #128c7e;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    font-size: 24px;
    margin-left: 10px;
  }
  .contact-info, .call-info {
    flex: 1;
  }
  .call-icon {
    margin-right: 10px;
    color: #075e54;
  }
  .keyboard {
    display: none;
    background-color: #f0f0f0;
    padding: 0px;
  }
  .keyboard-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 5px;
  }
  .key {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 10px;
    width: 30px;
    text-align: center;
    cursor: pointer;
  }
  .key:hover {
    background-color: #e0e0e0;
  }
  .space-key {
    width: 150px;
  }
  .backspace-key {
    width: 60px;
  }
</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>
  <div class="container" id="app">
    <div class="header">
      <h2 id="page-title">واتساپ</h2>
      <div class="header-icons">
        <i class="fas fa-search header-icon" onclick="showSearch()"></i>
        <div class="dropdown">
          <i class="fas fa-ellipsis-v header-icon" onclick="toggleDropdown()"></i>
          <div id="myDropdown" class="dropdown-content">
            <a onclick="showPage('new-group')">گروه جدید</a>
            <a onclick="showPage('new-broadcast')">پخش جدید</a>
            <a onclick="showPage('linked-devices')">دستگاه‌های متصل</a>
            <a  onclick="showPage('starred-messages')">پیام‌های ستاره‌دار</a>
            <a onclick="showPage('settings')">تنظیمات</a>
          </div>
        </div>
      </div>
    </div>
    
    <div class="content" id="content">
      <div id="chats-page">
        <div class="chat-list" id="chat-list"></div>
      </div>

      <div id="status-page" style="display: none;">
        <h3>وضعیت من</h3>
        <div class="status-item" onclick="updateStatus()">
          <div class="avatar">
            <i class="fas fa-plus"></i>
          </div>
          <div class="status-info">
            <h4>وضعیت من</h4>
            <p>برای به‌روزرسانی وضعیت کلیک کنید</p>
          </div>
        </div>
        <h3>به‌روزرسانی‌های اخیر</h3>
        <div id="status-list"></div>
      </div>

      <div id="calls-page" style="display: none;">
        <h3>تماس‌ها</h3>
        <div id="calls-list"></div>
      </div>

      <div id="contacts-page" style="display: none;">
        <h3>مخاطبان</h3>
        <div id="contacts-list"></div>
      </div>

      <div id="chat-page" style="display: none;">
        <div class="chat-window" id="chat-window"></div>
        <div class="message-input">
          <input type="text" id="message-input" placeholder="پیام خود را بنویسید..." readonly onclick="toggleKeyboard()">
          <button onclick="sendMessage()">ارسال</button>
        </div>
        <div class="keyboard" id="custom-keyboard">
          <div class="keyboard-row">
            <div class="key" onclick="addToInput('ض')">ض</div>
            <div class="key" onclick="addToInput('ص')">ص</div>
            <div class="key" onclick="addToInput('ث')">ث</div>
            <div class="key" onclick="addToInput('ق')">ق</div>
            <div class="key" onclick="addToInput('ف')">ف</div>
            <div class="key" onclick="addToInput('غ')">غ</div>
            <div class="key" onclick="addToInput('ع')">ع</div>
            <div class="key" onclick="addToInput('ه')">ه</div>
            <div class="key" onclick="addToInput('خ')">خ</div>
            <div class="key" onclick="addToInput('ح')">ح</div>
          </div>
          <div class="keyboard-row">
            <div class="key" onclick="addToInput('ش')">ش</div>
            <div class="key" onclick="addToInput('س')">س</div>
            <div class="key" onclick="addToInput('ی')">ی</div>
            <div class="key" onclick="addToInput('ب')">ب</div>
            <div class="key" onclick="addToInput('ل')">ل</div>
            <div class="key" onclick="addToInput('ا')">ا</div>
            <div class="key" onclick="addToInput('ت')">ت</div>
            <div class="key" onclick="addToInput('ن')">ن</div>
            <div class="key" onclick="addToInput('م')">م</div>
            <div class="key" onclick="addToInput('ک')">ک</div>
          </div>
          <div class="keyboard-row">
            <div class="key" onclick="addToInput('ظ')">ظ</div>
            <div class="key" onclick="addToInput('ط')">ط</div>
            <div class="key" onclick="addToInput('ز')">ز</div>
            <div class="key" onclick="addToInput('ر')">ر</div>
            <div class="key" onclick="addToInput('ذ')">ذ</div>
            <div class="key" onclick="addToInput('د')">د</div>
            <div class="key" onclick="addToInput('پ')">پ</div>
            <div class="key" onclick="addToInput('و')">و</div>
            <div class="key" onclick="addToInput('گ')">گ</div>
            <div class="key backspace-key" onclick="backspace()"><i class="fas fa-backspace"></i></div>
          </div>
          <div class="keyboard-row">
            <div class="key" onclick="addToInput('؟')">؟</div>
            <div class="key" onclick="addToInput('!')">!</div>
            <div class="key space-key" onclick="addToInput(' ')">فاصله</div>
            <div class="key" onclick="addToInput('،')">،</div>
            <div class="key" onclick="addToInput('.')">.</div>
          </div>
        </div>
      </div>

      <div id="settings-page" style="display: none;">
        <h3>تنظیمات</h3>
        <div class="setting-item" onclick="showPage('account')">
          <i class="fas fa-user"></i> حساب کاربری
        </div>
        <div class="setting-item" onclick="showPage('privacy')">
          <i class="fas fa-lock"></i> حریم خصوصی
        </div>
        <div class="setting-item" onclick="showPage('chats-settings')">
          <i class="fas fa-comments"></i> تنظیمات چت
        </div>
        <div class="setting-item" onclick="showPage('notifications')">
          <i class="fas fa-bell"></i> اعلان‌ها
        </div>
        <div class="setting-item" onclick="showPage('storage')">
          <i class="fas fa-database"></i> ذخیره‌سازی و داده‌ها
        </div>
        <div class="setting-item" onclick="showPage('help')">
          <i class="fas fa-question-circle"></i> راهنما
        </div>
      </div>

      <div id="new-group-page" style="display: none;">
        <h3>ایجاد گروه جدید</h3>
        <p>اینجا می‌توانید گروه جدید ایجاد کنید.</p>
      </div>

      <div id="new-broadcast-page" style="display: none;">
        <h3>ایجاد پخش جدید</h3>
        <p>اینجا می‌توانید پخش جدید ایجاد کنید.</p>
      </div>

      <div id="linked-devices-page" style="display: none;">
        <h3>دستگاه‌های متصل</h3>
        <p>لیست دستگاه‌های متصل به حساب شما اینجا نمایش داده می‌شود.</p>
      </div>

      <div id="starred-messages-page" style="display: none;">
        <h3>پیام‌های ستاره‌دار</h3>
        <p>پیام‌های ستاره‌دار شما اینجا نمایش داده می‌شود.</p>
      </div>

      <div id="account-page" style="display: none;">
        <h3>تنظیمات حساب کاربری</h3>
        <p>اینجا می‌توانید تنظیمات حساب کاربری خود را تغییر دهید.</p>
      </div>

      <div id="privacy-page" style="display: none;">
        <h3>تنظیمات حریم خصوصی</h3>
        <p>اینجا می‌توانید تنظیمات حریم خصوصی خود را تغییر دهید.</p>
      </div>

      <div id="chats-settings-page" style="display: none;">
        <h3>تنظیمات چت</h3>
        <p>اینجا می‌توانید تنظیمات چت خود را تغییر دهید.</p>
      </div>

      <div id="notifications-page" style="display: none;">
        <h3>تنظیمات اعلان‌ها</h3>
        <p>اینجا می‌توانید تنظیمات اعلان‌های خود را تغییر دهید.</p>
      </div>

      <div id="storage-page" style="display: none;">
        <h3>تنظیمات ذخیره‌سازی و داده‌ها</h3>
        <p>اینجا می‌توانید تنظیمات ذخیره‌سازی و داده‌های خود را مدیریت کنید.</p>
      </div>

      <div id="help-page" style="display: none;">
        <h3>راهنما</h3>
        <p>اینجا می‌توانید اطلاعات راهنما و پشتیبانی را مشاهده کنید.</p>
      </div>
    </div>

    <div class="bottom-nav">
      <div class="nav-item active" onclick="showPage('chats')">
        <i class="fas fa-comments"></i>
        <div>چت‌ها</div>
      </div>
      <div class="nav-item" onclick="showPage('status')">
        <i class="fas fa-circle"></i>
        <div>وضعیت</div>
      </div>
      <div class="nav-item" onclick="showPage('calls')">
        <i class="fas fa-phone"></i>
        <div>تماس‌ها</div>
      </div>
      <div class="nav-item" onclick="showPage('contacts')">
        <i class="fas fa-address-book"></i>
        <div>مخاطبان</div>
      </div>
    </div>
  </div>

  <script>
    const chatList = [
      { id: 1, name: "عبدالله چلاسی", lastMessage: "سلام، چطوری؟" },
      { id: 2, name: "دلفین گربدان", lastMessage: "فردا جلسه داریم" },
      { id: 3, name: "باشگاه قشم", lastMessage: "عکس‌ها رو فرستادم" }
    ];

    const chats = {
      1: [
        { sender: "عبدالله چلاسی", message: "سلام، چطوری؟" },
        { sender: "من", message: "سلام عبدالله چلاسی خوبم ممنون. تو چطوری؟" }
      ],
      2: [
        { sender: "ماجد", message: "فردا جلسه داریم" },
        { sender: "من", message: "باشه، ساعت چند؟" }
      ],
      3: [
        { sender: "عبدالقادر", message: "عکس‌ها رو فرستادم" },
        { sender: "من", message: "دستت درد نکنه، الان میبینم" }
      ]
    };

    const statusList = [
      { id: 1, name: "عبدالله چلاسی", time: "امروز 10:30", content: "در حال مطالعه 📚" },
      { id: 2, name: "محمد", time: "امروز 09:15", content: "سفر به شمال 🌳" },
      { id: 3, name: "فرشاد", time: "دیروز 23:45", content: "شب بخیر دوستان 🌙" }
    ];

    const callsList = [
      { id: 1, name: "عبدالله چلاسی", time: "امروز 14:20", type: "incoming" },
      { id: 2, name: "باشگاه قشم", time: "دیروز 18:45", type: "outgoing" },
      { id: 3, name: "دلفین گربدان", time: "2 روز پیش", type: "missed" },
      { id: 4, name: "قشم", time: "3 روز پیش", type: "incoming" },
      { id: 5, name: "عبدالقادر", time: "هفته پیش", type: "outgoing" }
    ];

    const contactsList = [
      { id: 1, name: "عبدالله چلاسی" },
      { id: 2, name: "عبدالقادر" },
      { id: 3, name: "وحید" },
      { id: 4, name: "عبدالعزیز" },
      { id: 5, name: "ماجد" },
      { id: 6, name: "امیر" },
      { id: 7, name: "فرشاد" },
      { id: 8, name: "یعقوب" },
      { id: 9, name: "ایوب" },
      { id: 10, name: "محمد" }
    ];

    function renderChatList() {
      const chatListElement = document.getElementById("chat-list");
      chatListElement.innerHTML = chatList.map(chat => `
        <div class="chat-item" onclick="openChat(${chat.id}, '${chat.name}')">
          <div class="avatar">${chat.name[0]}</div>
          <div class="contact-info">
            <h3>${chat.name}</h3>
            <p>${chat.lastMessage}</p>
          </div>
        </div>
      `).join("");
    }

    function renderStatusList() {
      const statusListElement = document.getElementById("status-list");
      statusListElement.innerHTML = statusList.map(status => `
        <div class="status-item" onclick="viewStatus(${status.id})">
          <div class="avatar">
            ${status.name[0]}
          </div>
          <div class="status-info">
            <h4>${status.name}</h4>
            <p>${status.time}</p>
          </div>
        </div>
      `).join("");
    }

    function renderCallsList() {
      const callsListElement = document.getElementById("calls-list");
      callsListElement.innerHTML = callsList.map(call => `
        <div class="call-item">
          <div class="avatar">${call.name[0]}</div>
          <div class="call-info">
            <h3>${call.name}</h3>
            <p>${call.time}</p>
          </div>
          <div class="call-icon">
            <i class="fas fa-phone${call.type === 'incoming' ? '-alt' : call.type === 'outgoing' ? '' : '-slash'}" style="color: ${call.type === 'missed' ? 'red' : '#075e54'}"></i>
          </div>
        </div>
      `).join("");
    }

    function renderContactsList() {
      const contactsListElement = document.getElementById("contacts-list");
      contactsListElement.innerHTML = contactsList.map(contact => `
        <div class="contact-item" onclick="openChat(${contact.id}, '${contact.name}')">
          <div class="avatar">${contact.name[0]}</div>
          <div class="contact-info">
            <h3>${contact.name}</h3>
          </div>
        </div>
      `).join("");
    }

    function openChat(chatId, chatName) {
      showPage('chat');
      document.getElementById("page-title").textContent = chatName;
      renderChat(chatId);
    }

    function renderChat(chatId) {
      const chatWindow = document.getElementById("chat-window");
      chatWindow.innerHTML = chats[chatId].map(message => `
        <div class="message ${message.sender === 'من' ? 'sent' : 'received'}">
          <p>${message.message}</p>
        </div>
      `).join("");
      chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    function showPage(pageId) {
      const pages = ['chats', 'status', 'calls', 'contacts', 'chat', 'settings', 'new-group', 'new-broadcast', 'linked-devices', 'starred-messages', 'account', 'privacy', 'chats-settings', 'notifications', 'storage', 'help'];
      pages.forEach(page => {
        document.getElementById(`${page}-page`).style.display = page === pageId ? 'block' : 'none';
      });

      if (pageId !== 'chat') {
        document.getElementById("page-title").textContent = getPageTitle(pageId);
      }

      document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
      });
      if (['chats', 'status', 'calls', 'contacts'].includes(pageId)) {
        document.querySelector(`.nav-item[onclick="showPage('${pageId}')"]`).classList.add('active');
      }

      if (pageId === 'status') {
        renderStatusList();
      } else if (pageId === 'calls') {
        renderCallsList();
      } else if (pageId === 'contacts') {
        renderContactsList();
      }
    }

    function getPageTitle(pageId) {
      const titles = {
        'chats': 'واتساپ',
        'status': 'وضعیت',
        'calls': 'تماس‌ها',
        'contacts': 'مخاطبان',
        'settings': 'تنظیمات',
        'new-group': 'گروه جدید',
        'new-broadcast': 'پخش جدید',
        'linked-devices': 'دستگاه‌های متصل',
        'starred-messages': 'پیام‌های ستاره‌دار',
        'account': 'حساب کاربری',
        'privacy': 'حریم خصوصی',
        'chats-settings': 'تنظیمات چت',
        'notifications': 'اعلان‌ها',
        'storage': 'ذخیره‌سازی و داده‌ها',
        'help': 'راهنما'
      };
      return titles[pageId] || 'واتساپ';
    }

    function sendMessage() {
      const input = document.getElementById("message-input");
      const message = input.value.trim();
      if (message) {
        const chatTitle = document.getElementById("page-title").textContent;
        const chatId = chatList.find(chat => chat.name === chatTitle).id;
        chats[chatId].push({ sender: "من", message: message });
        renderChat(chatId);
        input.value = "";
        
        setTimeout(() => {
          const responses = [
            "فروشگاه دیجی کد عالیه ؟",
            "من عبدالله چلاسی هستم",
            "لطفا فروشگاه دیجی کد رو به بقیه معرفی کنید",
            "به روز ترین فروشگاه دیجی کد که میتونید هم از برنامه استفاده کنید و هم کدهای برنامه رو میتونید مشاهده کنید",
            "لطفا نظرات خودتان را برام ارسال کنید",
            "چطوری رفیق",
            "ممنونم از اینکه فروشگاه دیجی کد رو دانلود کردی",
            "از فروشگاه دیجی کد راضی هستید",
            "سعی میکنم برنامه و بازی های بیشتری توی دیجی کد قرار بدم",
            "اگر وبسایتی یا ابلیکیشنی خواستی با این شماره تماس بگیر 09335825325"
          ];
          const replyMessage = responses[Math.floor(Math.random() * responses.length)];
          chats[chatId].push({ sender: chatTitle, message: replyMessage });
          renderChat(chatId);
        }, 1000 + Math.random() * 2000);
      }
    }

    function toggleDropdown() {
      document.getElementById("myDropdown").classList.toggle("show");
    }

    function showSearch() {
      alert("جستجو");
    }

    function updateStatus() {
      const newStatus = prompt("وضعیت جدید خود را وارد کنید:");
      if (newStatus) {
        alert(`وضعیت شما به '${newStatus}' تغییر کرد.`);
      }
    }

    function viewStatus(statusId) {
      const status = statusList.find(s => s.id === statusId);
      if (status) {
        alert(`نمایش وضعیت ${status.name}: ${status.content}`);
      }
    }

    function toggleKeyboard() {
      const keyboard = document.getElementById('custom-keyboard');
      keyboard.style.display = keyboard.style.display === 'none' ? 'block' : 'none';
    }

    function addToInput(char) {
      const input = document.getElementById('message-input');
      input.value += char;
    }

    function backspace() {
      const input = document.getElementById('message-input');
      input.value = input.value.slice(0, -1);
    }

    window.onclick = function(event) {
      if (!event.target.matches('.header-icon')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
          }
        }
      }
    }

    renderChatList();
    showPage('chats');
  </script>
</body>
</html>
""",height=850)












            
    with col3:
        with st.expander("دانلود ویدیوهای یوتیوب", expanded=True):
            st.image("ve.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("لینک ویدیو رو سرچ کنید و بعد از سرچ ویدیو باز میشه و ویدیو رو میتونید دانلود کنید")
            with col2:
                st.image("p.png",width=20)

            if st.button("نمایش کد برنامه Vetube"):
            
                st.code('''
import streamlit as st
from pytube import YouTube 
import re
st.set_page_config(page_title="وی تیوب",page_icon="logo.png",)
# with open('c.css') as f:
#     st.markdown(f"<style> {f.read()} </style>",unsafe_allow_html=True)
st.header("وی تیوب")
st.text("دانلود ویدیوهای یوتیوب")
st.write('لینک ویدیوی یوتیوب را جستجو کنید و ویدیو برای شما ارسال خواهد شد')
    
    
  
link = st.text_input("Enter URL : ",)
st.button("Search",link)
video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", link)
video_id = video_id_match.group(1) if video_id_match else None
if video_id:
   video = YouTube(f"https://www.youtube.com/watch?v={video_id}")
   available_streams = video.streams.filter(file_extension="mp4").all()
   stream_quality = st.selectbox("Select Video Quality", [str(stream.resolution) for stream in available_streams])
   if st.button("Download"):
       selected_stream = next((stream for stream in available_streams if str(stream.resolution) == stream_quality), None)
       if selected_stream:
           st.text("Downloading...")
           file_path = selected_stream.download()
           st.text("Download complete!")
           st.divider()
           st.write("Click to download the video and wait a few moments for the download to take effect")
           
           # Display video
           st.video(file_path)
       else:
           st.text("Selected video quality is not available.")
else:
   st.error("Search YouTube video link .")
st.markdown("ساخته شده توسط عبدالله چلاسی")
''')
            

            
            st.warning("برای اجرای برنامه به محیط برنامه نویسی نیاز دارید")


                
                





    with col3:
        with st.expander("تیمچت", expanded=True):
            st.image("chat.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("چت آنلاین با کمترین کدها فرستادن بیام و ذخیره شدن در دیتابیس")
            with col2:
                st.image("p.png",width=20)

        
            if st.button("نمایش کد برنامه تیمچت"):

                st.code(
     """import sqlite3
from datetime import datetime
import streamlit as st
# اتصال به پایگاه داده
conn = sqlite3.connect('chat.db')
c = conn.cursor()
# ایجاد جدول پیام‌ها اگر وجود نداشته باشد
c.execute('''CREATE TABLE IF NOT EXISTS messages
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT,
             message TEXT,
             timestamp DATETIME)''')
conn.commit()
# تابع افزودن پیام جدید
def add_message(username, message):
    timestamp = datetime.now().strftime(f"%Y-%m-% {"<->"} %H:%M:%S")
    c.execute("INSERT INTO messages (username, message, timestamp) VALUES (?, ?, ?)",
              (username, message, timestamp))
    conn.commit()
# تابع دریافت تمام پیام‌ها
def get_messages():
    c.execute("SELECT id, username, message, timestamp FROM messages ORDER BY timestamp DESC LIMIT 100")
    return c.fetchall()
# تابع حذف پیام
def delete_message(message_id):
    c.execute("DELETE FROM messages WHERE id = ?", (message_id,))
    conn.commit()
# ورود نام کاربری
username = st.text_input(": نام خود را وارد کنید")
# نمایش پیام‌های موجود
messages = get_messages()
# ورودی پیام جدید
new_message = st.text_input(": پیام خود را وارد کنید")
if st.button("ارسال") and username and new_message:
    add_message(username, new_message)
    st.rerun()
st.subheader("پیام‌ها")
for msg in reversed(messages):
    msg_id, msg_user, msg_text, msg_timestamp = msg
    st.success(f"{msg_timestamp} 🙋🏽‍♂️ {msg_user}: 💬 {msg_text}")
    
    # افزودن دکمه برای حذف پیام
    if st.button("حذف", key=f"delete_{msg_id}"):
        delete_message(msg_id)
        st.rerun()
# بستن اتصال به پایگاه داده
conn.close()
    """,language="python"
            )
                
            st.success("🔻 تیمچت 🔻")

            conn = sqlite3.connect('chat.db')
            c = conn.cursor()

                # ایجاد جدول پیام‌ها اگر وجود نداشته باشد
            c.execute('''CREATE TABLE IF NOT EXISTS messages
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT,
                            message TEXT,
                            timestamp DATETIME)''')
            conn.commit()

                # تابع افزودن پیام جدید
            def add_message(username, message):
                timestamp = datetime.now().strftime("%Y-%m-%  %H:%M:%S")
                c.execute("INSERT INTO messages (username, message, timestamp) VALUES (?, ?, ?)",
                            (username, message, timestamp))
                conn.commit()

                # تابع دریافت تمام پیام‌ها
            def get_messages():
                c.execute("SELECT id, username, message, timestamp FROM messages ORDER BY timestamp DESC LIMIT 100")
                return c.fetchall()

                # تابع حذف پیام
            def delete_message(message_id):
                c.execute("DELETE FROM messages WHERE id = ?", (message_id,))
                conn.commit()

                # ورود نام کاربری
            username = st.text_input(": نام خود را وارد کنید")

                # نمایش پیام‌های موجود
            messages = get_messages()

                # ورودی پیام جدید
            new_message = st.text_input(": پیام خود را وارد کنید")
            if st.button("ارسال") and username and new_message:
                add_message(username, new_message)
                st.rerun()

            for msg in reversed(messages):
                msg_id, msg_user, msg_text, msg_timestamp = msg
                st.success(f"{msg_timestamp} 🙋🏽‍♂️ {msg_user}: 💬 {msg_text}")
                    
                    # افزودن دکمه برای حذف پیام
                if st.button("حذف", key=f"delete_{msg_id}"):
                    delete_message(msg_id)
                    st.rerun()

                # بستن اتصال به پایگاه داده
            conn.close()

            









    with col3:
        with st.expander("آخرین خبرهای ورزشی", expanded=True):
            st.image("kh.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("آخرین خبرهای ورزشی رو دنبال کنید")
            with col2:
                st.image("p.png",width=20)
            if st.button("نمایش کد برنامه آخرین خبرهای ورزشی"):
                st.code("""
   import streamlit as st
import requests
st.set_page_config(page_title="اخبار ورزشی",page_icon="https://myket.ir/app-icon/ir.gharivand.breakingnews_6266d09a-0c19-46c3-ae5b-edf65278623e.png")
st.title("اخبار ورزشی")
st.image("https://myket.ir/app-icon/ir.gharivand.breakingnews_6266d09a-0c19-46c3-ae5b-edf65278623e.png")
text = st.text_input(" اخبار کدام تیم رو دنبال میکنید ؟")
r = requests.get(f'https://search-api.varzesh3.com/v1.0/query?q={text}')
x= r.json()
for i in x['news'] :
    st.subheader(i['title'])
    st.success(i['persianPublishedOn'])
    st.image(i['picture'])
    st.write(i['shortDescription'])
    st.write('--------')
st.warning("طراح و برنامه نویس : عبدالله چلاسی")
    """,language="python")
                

            st.success("🔻 آخرین خبرهای ورزشی 🔻")


            text = st.text_input(" اخبار کدام تیم رو دنبال میکنید ؟")


            r = requests.get(f'https://search-api.varzesh3.com/v1.0/query?q={text}')

            x= r.json()

            st.button("جستجو")

            for i in x['news'] :
                st.subheader(i['title'])
                st.success(i['persianPublishedOn'])
                st.image(i['picture'])
                st.write(i['shortDescription'])
                st.write('--------')

                


    with col3:
        with st.expander("خدمات ایزوگام گربدان", expanded=True):
            st.image("izogam.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("اضافه کردن و ویرایش و حذف محصولات : این بروزه برای مدیریت کردن محصولات خود استفاده کنید و هم میتونید برای مشتری بزنید کافیه تغییراتی انجام بدید که برای مشتری مناسب باشه و از این طریق هم درآمد کسب کنید")
            with col2:
                st.image("p.png",width=20)
            if st.button("نمایش کد برنامه ایزوگام"):

                st.code("""
   import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu
con=sqlite3.connect('picscols.db')
cur=con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS pics(id TEXT, img BLOB, note TEXT)')
st.set_page_config(page_title="خدمات ایزوگام گربدان", page_icon="https://ayeghariya.com/wp-content/uploads/2023/01/%D8%A7%DB%8C%D8%B2%D9%88%DA%AF%D8%A7%D9%85-%DA%86%DB%8C%D8%B3%D8%AA.jpg")
st.text("ایزوگام گربدان")
selected = option_menu (
    menu_title=None,
    options=["ورود ادمین","صفحه اصلی"],
    icons=["book","house" ],
    menu_icon="cast",
    default_index=1,
    orientation="horizontal",
    styles={
        
        "nav-link":{
            'font-family': 'Courier New' 'Courier' 'monospace'
        },
        
    }
)
with st.expander("خدمات ایزوگام - گربدان",expanded=True):
   
    st.write("خدمات ایزوگام جزیره با ۱۰ سال ضمانت با مدیریت عبدالله چلاسی 09335825325")
        
      
 
 
if selected == "ورود ادمین":
	username = st.text_input(label="نام کاربری",placeholder="Username")
	password = st.text_input(label="پسورد",placeholder="password",type="password")
	btnLogin = st.button("ورود")
	if username == "admin" and password == "admin":
        
		st.success("خوش آمدی ادمین")
        
		selected = option_menu(options=["پست های ادمین"],
        menu_title=""
        
        
        )
		
	elif username or password == "admin":
		st.error("لطفا درست وارد کنید")
 
 
  
 
 
if selected == "پست های ادمین":
    
    st.success("توجه : لطفا با اضافه کردن محصول محصولات خود رو کامل پر کنید (عکس محصول , کد محصول , نام محصول) این ها نباید خالی باشد")
    st.error("هشدار : کد و نام محصولات شما نباید مثل محصولات دیگه ای که اضافه میکنید باشد. کد محصولات رو با اعداد انگلیسی و از شماره بالا به پایین شروع کنید . مانند : ( از 999 شروع کنید به پایین) ")
    
    if st.button('اضافه کردن محصول'):
        cur.execute('INSERT INTO pics(id, img, note) VALUES(?,?,?)', ('', '', ''))
        con.commit()
     
    
    st.write('---')
    for row in cur.execute('SELECT rowid, id, img, note FROM pics ORDER BY id'):
        with st.form(f'ID-{row[0]}',clear_on_submit=True):
            imgcol, notecol = st.columns([3, 2])
            id=notecol.text_input('کد محصول', row[1])
            note=notecol.text_area('نام محصول', row[3])
            if row[2]:
                img=row[2] 
                imgcol.image(row[2]) 
            file=imgcol.file_uploader('تصاویر', ['png', 'jpg', 'gif','jpeg', 'bmp'])
            if file:  
                img=file.read()
            if notecol.form_submit_button('ذخیره محصول'):
                
                cur.execute(
                    'UPDATE pics SET id=?, img=?, note=? WHERE id=?;', 
                    (id, img, note, str(row[1]))
                    )
            
                con.commit()
                st.experimental_rerun()
             
            
                
            if notecol.form_submit_button("حذف محصول"):
                cur.execute(f'''DELETE FROM pics WHERE rowid="{row[0]}";''')
                con.commit()
                st.experimental_rerun()
        
if selected == "صفحه اصلی":
     
     
     
     for row in cur.execute('SELECT rowid, id, img, note FROM pics ORDER BY id'):
        # with st.form(f'ID-{row[0]}', clear_on_submit=True):
        st.write("---")
        imgcol, notecol = st.columns([3, 2])
        # id=notecol.text_input('id', row[1])
        id=notecol.text_input('کد محصول', row[1])
        note=notecol.text_area('اسم محصول', row[3])
        if row[2]:
            img=row[2]
            imgcol.image(row[2])
            
        
            
    
st.write("---")
st.markdown("طراح و برنامه نویس : عبداالله چلاسی")
            
    
    """,language="python")
                
            st.success("🔻 خدمات ایزوگام گربدان 🔻")

            
            
            con=sqlite3.connect('picscols.db')
            cur=con.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS pics(id TEXT, img BLOB, note TEXT)')



            selected = option_menu (
                menu_title=None,
                options=["ورود ادمین","صفحه اصلی"],
                icons=["book","house" ],
                menu_icon="cast",
                default_index=1,
                orientation="horizontal",
                styles={

                    
                    "nav-link":{
                        'font-family': 'Courier New' 'Courier' 'monospace',
                        "font-size": "13px"
                    },
                    
                }
            )



            
            st.write("خدمات ایزوگام جزیره با ۱۰ سال ضمانت با مدیریت عبدالله چلاسی 09335825325")
                    

                
            
            





            if selected == "ورود ادمین":

                username = st.text_input(label="نام کاربری",placeholder="Username")
                password = st.text_input(label="پسورد",placeholder="password",type="password")
                btnLogin = st.button("ورود")

                if username == "admin" and password == "admin":
                    
                    st.success("خوش آمدی ادمین")
                    
                    selected = option_menu(options=["پست های ادمین"],
                    menu_title=""

                    
                    
                    )
                    
                elif username or password == "admin":
                    st.error("لطفا درست وارد کنید")



            
            
            
            


            

            if selected == "پست های ادمین":
                
                st.success("توجه : لطفا با اضافه کردن محصول محصولات خود رو کامل پر کنید (عکس محصول , کد محصول , نام محصول) این ها نباید خالی باشد")
                st.error("هشدار : کد و نام محصولات شما نباید مثل محصولات دیگه ای که اضافه میکنید باشد. کد محصولات رو با اعداد انگلیسی و از شماره بالا به پایین شروع کنید . مانند : ( از 999 شروع کنید به پایین) ")
                
                if st.button('اضافه کردن محصول'):
                    cur.execute('INSERT INTO pics(id, img, note) VALUES(?,?,?)', ('', '', ''))
                    con.commit()
                
                

                st.write('---')

                for row in cur.execute('SELECT rowid, id, img, note FROM pics ORDER BY id'):
                    with st.form(f'ID-{row[0]}',clear_on_submit=True):
                        imgcol, notecol = st.columns([3, 2])
                        id=notecol.text_input('کد محصول', row[1])
                        note=notecol.text_area('نام محصول', row[3])
                        if row[2]:
                            img=row[2] 
                            imgcol.image(row[2]) 
                        file=imgcol.file_uploader('تصاویر', ['png', 'jpg', 'gif','jpeg', 'bmp'])
                        if file:  
                            img=file.read()
                        if notecol.form_submit_button('ذخیره محصول'):
                            
                            cur.execute(
                                'UPDATE pics SET id=?, img=?, note=? WHERE id=?;', 
                                (id, img, note, str(row[1]))
                                )
                        
                            con.commit()
                            st.experimental_rerun()
                        
                        
                            
                        if notecol.form_submit_button("حذف محصول"):
                            cur.execute(f'''DELETE FROM pics WHERE rowid="{row[0]}";''')
                            con.commit()
                            st.experimental_rerun()

                    


            if selected == "صفحه اصلی":



                


                

                

                for row in cur.execute('SELECT rowid, id, img, note FROM pics ORDER BY id'):
                    # with st.form(f'ID-{row[0]}', clear_on_submit=True):
                    st.write("---")
                    imgcol, notecol = st.columns([3, 2])
                    # id=notecol.text_input('id', row[1])
                    id=notecol.text_input('کد محصول', row[1])
                    note=notecol.text_area('اسم محصول', row[3])
                    if row[2]:
                        img=row[2]
                        imgcol.image(row[2])
              














if menu_id == "ارز":

    st.divider()

    col1,col3 = st.columns(2)

        
        
    with col3:
        with st.expander("✨ قیمت ارز دیجیتال", expanded=True):
            st.image("qarz.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("نمایش آخرین قیمت ارز دیجیتال به دلار , قیمت رو به صورت لحظه ای مشاهده کنید")
            with col2:
                st.image("p.png",width=20)
            if st.button("نمایش کد قیمت ارز"):

                st.code(
                '''
    import streamlit as st
    import requests
    def get_crypto_price(crypto):
        # درخواست اطلاعات ارز دیجیتال از وبسرویس
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        # استخراج قیمت ارز دیجیتال
        price = data[crypto]["usd"]
        # نمایش قیمت ارز دیجیتال
        st.write(f"قیمت {crypto}: {price} دلار")
    # تنظیم صفحه
    st.title("برنامه ارز دیجیتال")
    crypto = st.text_input("نام ارز دیجیتال (مثال: bitcoin, ethereum)")
    if st.button("دریافت قیمت"):
        get_crypto_price(crypto)
        if not crypto :
            st.error("لطفا درست وارد کن")
    st.warning("طراحی شده توسط عبدالله چلاسی")
    ''',language="python"
            )
                
            st.warning("برای اجرای برنامه به محیط برنامه نویسی نیاز دارید")









                
    


st.divider()
st.markdown("فروشگاه دیجی کد متعلق به عبداالله چلاسی می باشد")
