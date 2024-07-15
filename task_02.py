'''Draws a Koch snowflake '''
import turtle

t = turtle.Turtle()
t.speed(10)
# turtle.tracer(False)

def draw_kochs_line(length, n):
    '''Draws a Koch curve using a recursive call'''
    if n == 0:
        t.forward(length)
    else:
        for angle in [0, 60, -120, 60]:
            t.right(angle)
            draw_kochs_line(length / 3, n - 1)

def get_order(s, message="Введіть рівень рекурсії (0-6):") -> int:
    '''Requesting the recursion level from the user through the graphical window'''
    order = s.textinput("Рівень рекурсії", message)
    if order is not None:
        try:
            order = int(order)
            if order < 0 or order > 6:
                return get_order(s, message="Рівень рекурсії має бути між 0 та 6.")
        except ValueError:
            return get_order(s, message="Тут має бути число від 0 до 6!")
        return order

def main():

    screen = turtle.Screen()
    screen.setup(700, 700)
    screen.title("Сніжинка Коха")

    size = 300
    order = get_order(screen)

    # Setup start position
    t.penup()
    t.goto(-size / 2, -size * 3**0.5 / 6)
    t.pendown()

    # Draw the Snowflake
    for _ in range(3):
        draw_kochs_line(size, order)
        t.left(120)

    turtle.done()

if __name__ == "__main__":
    main()
