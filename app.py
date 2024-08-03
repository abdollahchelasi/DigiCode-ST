import streamlit as st
from streamlit_option_menu import option_menu
import hydralit_components as hc
import streamlit.components.v1 as components
import sqlite3
from datetime import datetime




st.set_page_config(page_title="فروشگاه دیجی کد", layout="wide",page_icon="digicode.png")



with open("c.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

st.image("digicode.png",width=200)

menu_data = [

    
    {'id':"صفحه اصلی",'icon': "🏠", 'label':"صفحه اصلی",},

    {"id": "ساخت بازی", "icon": "🎮", "label": "ساخت بازی"},
    {'id':"ساخت برنامه",'icon':"📳",'label':"ساخت وب اپلیکیشن"},
    {'id':"ارز",'icon': "₿", 'label':"ارز"},
    
]

menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme={'txc_inactive': 'white','menu_background':'#133769','txc_active':'yellow','option_active':'#2967a8'},
    
#     home_name='Home',
#     login_name='Logout',
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned

)


















if menu_id == "صفحه اصلی":

    selected = option_menu (
      menu_title=None,
      options=[ "راهنما","صفحه اصلی"],
      icons=["book","house" ],
      menu_icon="cast",
      default_index=1,
      orientation="horizontal",

      styles={
         "container": {"background-color": "#133769"},
         "nav-link-selected": {"background-color": "#040b3e"},
         "nav-link": {"font-size": "20px", "text-align": "center_y: 0.0", "margin":"0px", "--hover-color": "#afb8fb"},

        }
    )

    if selected == "صفحه اصلی":

        
        st.markdown("# :rainbow[فروشگاه آموزشی دیجی کد یکی از بزرگترین مرجع آموزشی ساخت وب اپلیکیشن و بازی برای همه]")

        st.divider()


        
            


    if selected == "راهنما":

        st.warning("""
توجه : اگر میخواین کدها رو اجرا کنید و برای دیگران بفرستید کافیه تو سایت Replit ثبت نام کنید و یک پروژه streamlit ایجاد کنید و کدهایی که در اختیار شما قرار دادم رو توی پروژه قرار بدید و تغییراتی که میخواین اعمال کنید و اجرا کنید و بعد میتونید لینک وبسایت رو برای دیگران بفرستید
""") 


if menu_id == "ساخت بازی":

    st.text("ساخت بازی")

    c1 , c2 = st.columns(2)

    with c1:
        with st.expander("بازی TicTakToe", expanded=True):
            st.image("Gtic.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("ساخت بازی تیک تاک تو یک بازی که با کامبیوتر بازی میکنید")
                st.image("p.png",width=20)
            st.code("""
    
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
    """,language="python")
            
            st.warning("برای اجرای بازی به محیط برنامه نویسی نیاز دارید")



    with c2:
        with st.expander("بازی مار", expanded=True):
            st.image("snake.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("ساخت مار بازی با خوردن دانه مار بزگتر میشه و شما نباید مار به خودش برخورد کنه اگر برخورد کرد بازی میسوزه و مجددا بازی شروع میشه")
                st.image("jsss.png",width=20)
            st.code("""
    <!DOCTYPE html>
<html lang="fa">
<head>
    <base href="https://desktop.websim.ai/" />
    <title>Snake Game with Buttons</title>
    <meta charset="UTF-8">
    <style>
        html, body {
            height: 100%;
            margin: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            # background-color: #f0f0f0;
            font-family: Arial, sans-serif;
        }

        #game-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
            max-width: 100%;
            padding: 10px;
            box-sizing: border-box;
        }

        canvas {
            border: 1px solid #ccc;
            margin-bottom: 20px;
            max-width: 100%;
            height: auto;
        }

        #controls {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 5px; /* فاصله بین دکمه‌ها کاهش یافته */
            width: 100%;
            max-width: 300px; /* حداکثر عرض کنترل‌ها */
        }

        button {
            width: 100%;
            height: 60px;
            font-size: 18px; /* اندازه فونت کاهش یافته */
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color: #45a049;
        }

        button:active {
            background-color: #3e8e41;
        }

        @media (max-width: 600px) {
            #controls {
                gap: 5px; /* فاصله بین دکمه‌ها کاهش یافته */
            }
            button {
                height: 50px; /* ارتفاع دکمه‌ها کاهش یافته */
                font-size: 16px; /* اندازه فونت کاهش یافته */
            }
        }
    </style>
</head>
<body>
<div id="game-container">
    <canvas width="400" height="400" id="game"></canvas>
    <div id="controls">
        <button id="left">←</button>
        <button id="up">↑</button>
        </br>
        <button id="down">↓</button>
        <button id="right">→</button>
    </div>
</div>

<script>
var canvas = document.getElementById('game');
var context = canvas.getContext('2d');

var grid = 16;
var count = 0;

var snake = {
    x: 160,
    y: 160,
    dx: grid,
    dy: 0,
    cells: [],
    maxCells: 4
};

var apple = {
    x: 320,
    y: 320
};

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

function loop() {
    requestAnimationFrame(loop);

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

    context.fillStyle = 'green';
    snake.cells.forEach(function (cell, index) {
        context.fillRect(cell.x, cell.y, grid - 1, grid - 1);

        if (cell.x === apple.x && cell.y === apple.y) {
            snake.maxCells++;
            apple.x = getRandomInt(0, 25) * grid;
            apple.y = getRandomInt(0, 25) * grid;
        }

        for (var i = index + 1; i < snake.cells.length; i++) {
            if (cell.x === snake.cells[i].x && cell.y === snake.cells[i].y) {
                snake.x = 160;
                snake.y = 160;
                snake.cells = [];
                snake.maxCells = 4;
                snake.dx = grid;
                snake.dy = 0;

                apple.x = getRandomInt(0, 25) * grid;
                apple.y = getRandomInt(0, 25) * grid;
            }
        }
    });
}

function changeDirection(dx, dy) {
    if (dx !== -snake.dx && dy !== -snake.dy) {
        snake.dx = dx;
        snake.dy = dy;
    }
}

document.addEventListener('keydown', function (e) {
    if (e.which === 37 && snake.dx === 0) {
        changeDirection(-grid, 0);
    } else if (e.which === 38 && snake.dy === 0) {
        changeDirection(0, -grid);
    } else if (e.which === 39 && snake.dx === 0) {
        changeDirection(grid, 0);
    } else if (e.which === 40 && snake.dy === 0) {
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

requestAnimationFrame(loop);
</script>
</body>
</html>

    """,language="javascript")
            
            
            if st.button("اجرا کنید"):


                components.html(
    """
<!DOCTYPE html>
<html lang="fa">
<head>
    <base href="https://desktop.websim.ai/" />
    <title>Snake Game with Buttons</title>
    <meta charset="UTF-8">
    <style>
        html, body {
            height: 100%;
            margin: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            # background-color: #f0f0f0;
            font-family: Arial, sans-serif;
        }

        #game-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
            max-width: 100%;
            padding: 10px;
            box-sizing: border-box;
        }

        canvas {
            border: 1px solid #ccc;
            margin-bottom: 20px;
            max-width: 100%;
            height: auto;
        }

        #controls {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 5px; /* فاصله بین دکمه‌ها کاهش یافته */
            width: 100%;
            max-width: 300px; /* حداکثر عرض کنترل‌ها */
        }

        button {
            width: 100%;
            height: 60px;
            font-size: 18px; /* اندازه فونت کاهش یافته */
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color: #45a049;
        }

        button:active {
            background-color: #3e8e41;
        }

        @media (max-width: 600px) {
            #controls {
                gap: 5px; /* فاصله بین دکمه‌ها کاهش یافته */
            }
            button {
                height: 50px; /* ارتفاع دکمه‌ها کاهش یافته */
                font-size: 16px; /* اندازه فونت کاهش یافته */
            }
        }
    </style>
</head>
<body>
<div id="game-container">
    <canvas width="400" height="400" id="game"></canvas>
    <div id="controls">
        <button id="left">←</button>
        <button id="up">↑</button>
        </br>
        <button id="down">↓</button>
        <button id="right">→</button>
    </div>
</div>

<script>
var canvas = document.getElementById('game');
var context = canvas.getContext('2d');

var grid = 16;
var count = 0;

var snake = {
    x: 160,
    y: 160,
    dx: grid,
    dy: 0,
    cells: [],
    maxCells: 4
};

var apple = {
    x: 320,
    y: 320
};

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

function loop() {
    requestAnimationFrame(loop);

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

    context.fillStyle = 'green';
    snake.cells.forEach(function (cell, index) {
        context.fillRect(cell.x, cell.y, grid - 1, grid - 1);

        if (cell.x === apple.x && cell.y === apple.y) {
            snake.maxCells++;
            apple.x = getRandomInt(0, 25) * grid;
            apple.y = getRandomInt(0, 25) * grid;
        }

        for (var i = index + 1; i < snake.cells.length; i++) {
            if (cell.x === snake.cells[i].x && cell.y === snake.cells[i].y) {
                snake.x = 160;
                snake.y = 160;
                snake.cells = [];
                snake.maxCells = 4;
                snake.dx = grid;
                snake.dy = 0;

                apple.x = getRandomInt(0, 25) * grid;
                apple.y = getRandomInt(0, 25) * grid;
            }
        }
    });
}

function changeDirection(dx, dy) {
    if (dx !== -snake.dx && dy !== -snake.dy) {
        snake.dx = dx;
        snake.dy = dy;
    }
}

document.addEventListener('keydown', function (e) {
    if (e.which === 37 && snake.dx === 0) {
        changeDirection(-grid, 0);
    } else if (e.which === 38 && snake.dy === 0) {
        changeDirection(0, -grid);
    } else if (e.which === 39 && snake.dx === 0) {
        changeDirection(grid, 0);
    } else if (e.which === 40 && snake.dy === 0) {
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

requestAnimationFrame(loop);
</script>
</body>
</html>
    """,height=600
)






if menu_id == "ساخت برنامه":

    col1,col3,col4 = st.columns(3)




    with col1:
        with st.expander("✨ فوتو قشمی", expanded=True):
            st.image("photo.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("برنامه ویرایش عکس که میتونید فایل مورد نظر رو آپلود کنید و عرض و ارتفاع آن را مشخص کنید و فایل ویرایش شده رو دانلود کنید")
            with col2:
                st.image("p.png",width=20)
            st.code("""
    import streamlit as st
    from PIL import Image
    import base64
    from io import BytesIO

    def main():
        st.title("فوتو قشمی")
        st.write("با استفاده از این برنامه، می‌توانید تصویری را بارگذاری کنید و آن را بزرگنمایی کنید.")

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
    """,language="python")

            
    with col3:
        with st.expander("دانلود ویدیوهای یوتیوب", expanded=True):
            st.image("ve.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("لینک ویدیو رو سرچ کنید و بعد از سرچ ویدیو باز میشه و ویدیو رو میتونید دانلود کنید")
            with col2:
                st.image("p.png",width=20)
            
            st.code("""
import streamlit as st
from pytube import YouTube 
import re

st.set_page_config(page_title="وی تیوب",page_icon="logo.png",)

# with open('c.css') as f:
#     st.markdown(f"<style> {f.read()} </style>",unsafe_allow_html=True)



st.header("وی تیوب")
st.text("دانلود ویدیوهای یوتیوب")
st.write("
لینک ویدیوی یوتیوب را جستجو کنید و ویدیو برای شما ارسال خواهد شد")
    
    
  

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
""")




    with col3:
        with st.expander("گربدان چت", expanded=True):
            st.image("chat.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("چت آنلاین با کمترین کدها فرستادن بیام و ذخیره شدن در دیتابیس")
            with col2:
                st.image("img/p.png",width=20)
            st.code(
                """
    import sqlite3
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
    st.experimental_rerun()

st.subheader("پیام‌ها")
for msg in reversed(messages):
    msg_id, msg_user, msg_text, msg_timestamp = msg
    st.success(f"{msg_timestamp} 🙋🏽‍♂️ {msg_user}: 💬 {msg_text}")
    
    # افزودن دکمه برای حذف پیام
    if st.button("حذف", key=f"delete_{msg_id}"):
        delete_message(msg_id)
        st.experimental_rerun()

# بستن اتصال به پایگاه داده
conn.close()
    """,language="python"
            )

            


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
                st.experimental_rerun()

            st.subheader("پیام‌ها")
            for msg in reversed(messages):
                msg_id, msg_user, msg_text, msg_timestamp = msg
                st.success(f"{msg_timestamp} 🙋🏽‍♂️ {msg_user}: 💬 {msg_text}")
                
                # افزودن دکمه برای حذف پیام
                if st.button("حذف", key=f"delete_{msg_id}"):
                    delete_message(msg_id)
                    st.experimental_rerun()

            # بستن اتصال به پایگاه داده
            conn.close()











    with col4:
        with st.expander("آخرین خبرهای ورزشی", expanded=True):
            st.image("kh.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("آخرین خبرهای ورزشی رو دنبال کنید")
            with col2:
                st.image("p.png",width=20)
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




    with col4:
        with st.expander("خدمات ایزوگام گربدان", expanded=True):
            st.image("izogam.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("اضافه کردن و ویرایش و حذف محصولات : این بروزه برای مدیریت کردن محصولات خود استفاده کنید و هم میتونید برای مشتری بزنید کافیه تغییراتی انجام بدید که برای مشتری مناسب باشه و از این طریق هم درآمد کسب کنید")
            with col2:
                st.image("p.png",width=20)
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























if menu_id == "ارز":

    col1,col3 = st.columns(2)


            

    with col1:
        with st.expander("✨ وبسایت ارز دیجیتال", expanded=True):
            st.image("arz.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("نمایش آخرین چارت نماد های ارز دیجیتال")
            with col2:
                st.image("p.png",width=20)
            st.code("""
    import pandas as pd
    import streamlit as st
    import yfinance as yf


    st.title("ABDOLLAH ( crypto )")
    st.warning("نمایش چارت نماد های ارز دیجیتال")





    tickers = ["ETH-USD","TSLA","BTC-USD"]




    drop = st.multiselect("نماد رو انتخاب کنید",tickers)

    start = st.date_input('از تاریخ',value=pd.to_datetime("2018-01-01"))
    end = st.date_input('تا تاریخ',value=pd.to_datetime('today'))

    if len(drop)>0:
        df = yf.download(drop,start,end)['Adj Close']
        st.line_chart(df)



    st.error("ساخته شده توسط عبدالله چلاسی")
    """,language="python")

            
                    
        
    with col3:
        with st.expander("✨ قیمت ارز دیجیتال", expanded=True):
            st.image("qarz.png")
            col1,col2=st.columns([5,1])
            with col1:    
                st.caption("نمایش آخرین قیمت ارز دیجیتال به دلار , قیمت رو به صورت لحظه ای مشاهده کنید")
            with col2:
                st.image("p.png",width=20)
            st.code(
                """
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
    """,language="python"
            )
                
    


st.divider()
st.markdown("[فروشگاه دیجی کد متعلق به عبداالله چلاسی می باشد](https://abdollah-chelasi.hf.space)")
