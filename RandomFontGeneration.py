import turtle
import random
from math import cos, sin, pi


def BoxGeneration(width, height, start):
    # type: (object, object, list) -> None
    box_turtle = turtle.Turtle()
    # box_turtle.shape("turtle")
    box_turtle.speed(10)
    box_turtle.ht()
    box_turtle.st()
    box_turtle.up()
    box_turtle.goto(start[0], start[1])
    for i in range(0, 2):
        box_turtle.down()
        print(box_turtle.pos())
        box_turtle.forward(width)
        print(box_turtle.pos())
        box_turtle.right(90)
        box_turtle.forward(height)
        box_turtle.right(90)
        box_turtle.up()
    box_turtle.ht()


def drawA(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    a_turtle = turtle.Turtle()
    a_turtle.speed(10)
    # a_turtle.shape("turtle")
    a_turtle.ht()
    a_turtle.pensize(pensize)
    a_turtle.up()  # Initializing Turtle
    a_turtle.setpos(start[0] + width, start[1] - height)
    a_turtle.down()
    top_point = random.randint(start[0], start[0] + width)
    a_turtle.goto(top_point, start[1])
    a_turtle.goto(start[0], start[1] - height)
    a_turtle.up()
    cross_line_height = random.randint(start[1] - height, start[1])
    cross_line_width = random.randint(0, width)
    a_turtle.goto(top_point, cross_line_height)
    a_turtle.seth(0)
    a_turtle.down()
    a_turtle.forward(cross_line_width // 2)
    a_turtle.backward(cross_line_width)
    if serifs:
        a_turtle.up()
        a_turtle.goto(start[0] + width, start[1] - height)  # lower left pos
        serifsize = random.randint(5, 30)
        a_turtle.seth(0)
        a_turtle.down()
        a_turtle.forward(serifsize // 2)
        a_turtle.up()
        a_turtle.goto(start[0] + width, start[1] - height)  # lower left serif
        a_turtle.down()
        a_turtle.backward(serifsize // 2)
        a_turtle.up()
        a_turtle.goto(start[0], start[1] - height)  # lower right pos
        a_turtle.down()
        a_turtle.seth(0)
        a_turtle.forward(serifsize // 2)
        a_turtle.up()
        a_turtle.goto(start[0], start[1] - height)  # lower right serif
        a_turtle.down()
        a_turtle.backward(serifsize // 2)


def drawB(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    b_turtle = turtle.Turtle()
    b_turtle.speed(10)
    # b_turtle.shape("turtle")
    b_turtle.ht()
    b_turtle.pensize(pensize)
    b_turtle.up()
    b_turtle.setpos(start[0], start[1] - height)
    b_turtle.down()
    b_turtle.goto(start[0], start[1])
    b_turtle.seth(90)
    b_turtle.goto(start[0] + (width / 2), start[1])
    b_turtle.seth(-180)
    midy_top = random.randint(10, height)
    midy_bottom = height - midy_top
    r1 = midy_top // 2
    r2 = midy_bottom // 2
    b_turtle.circle(r1, -180)
    b_turtle.seth(-180)
    cross = random.randint(0, width // 2)
    b_turtle.forward(cross)
    b_turtle.up()
    b_turtle.back(cross)
    b_turtle.down()
    b_turtle.circle(r2, -180)
    b_turtle.goto(start[0], start[1] - height)
    if serifs:
        serifsize = random.randint(5, 30)
        b_turtle.up()
        b_turtle.goto(start[0], start[1])
        b_turtle.seth(0)
        b_turtle.goto(start[0], start[1]-height)
        b_turtle.down()
        b_turtle.back(serifsize // 2)
        b_turtle.up()
        b_turtle.goto(start[0], start[1])
        b_turtle.down()
        b_turtle.back(serifsize // 2)


def drawC(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) -> None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    c_turtle = turtle.Turtle()
    c_turtle.speed(10)
    # c_turtle.shape("turtle)
    c_turtle.ht()
    c_turtle.pensize(pensize)
    c_turtle.up()
    posx, posy = 0, 0
    for i in range(0, 180):
        posx += cos(i * pi / 180) * width / 58
        posy += sin(i * pi / 180) * height / 114
        c_turtle.goto((start[0] + width) - posx, start[1] - posy)
        c_turtle.down()
    c_turtle.up()
    if serifs:
        c_turtle.goto(start[0] + width, start[1])
        serifsize = random.randint(5, 20)
        c_turtle.seth(270)
        c_turtle.forward(serifsize // 2)
        c_turtle.down()
        c_turtle.back(serifsize)


def drawD(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    d_turtle = turtle.Turtle()
    d_turtle.speed(10)
    # d_turtle.shape("turtle")
    d_turtle.ht()
    d_turtle.pensize(pensize)
    d_turtle.up()
    d_turtle.setpos(start[0], start[1] - height)
    d_turtle.down()
    d_turtle.setpos(start[0], start[1])
    d_turtle.goto(start[0] + (width / 2), start[1])
    d_turtle.seth(-180)
    d_turtle.circle(height // 2, -180)
    d_turtle.seth(-180)
    d_turtle.goto(start[0], start[1] - height)
    if serifs:
        serifsize = random.randint(5, 30)
        d_turtle.up()
        d_turtle.goto(start[0], start[1])
        d_turtle.seth(0)
        d_turtle.goto(start[0], start[1]-height)
        d_turtle.down()
        d_turtle.back(serifsize // 2)
        d_turtle.up()
        d_turtle.goto(start[0], start[1])
        d_turtle.seth(0)
        d_turtle.down()
        d_turtle.back(serifsize // 2)


def drawE(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    e_turtle = turtle.Turtle()
    e_turtle.speed(10)
    # e_turtle.shape("turtle")
    e_turtle.ht()
    e_turtle.pensize(pensize)
    e_turtle.up()
    e_turtle.setpos(start[0], start[1] - height)
    e_turtle.down()
    e_turtle.goto(start[0], start[1])
    e_turtle.goto(start[0] + width, start[1])
    e_turtle.up()
    mid_h = random.randint(10, height // 2)
    mid_w = random.randint(width // 2, width)
    e_turtle.goto(start[0] + mid_w, start[1] - mid_h)
    e_turtle.down()
    e_turtle.back(random.randint(0, width))
    e_turtle.up()
    e_turtle.goto(start[0] + width, start[1] - height)
    e_turtle.down()
    e_turtle.goto(start[0], start[1] - height)
    if serifs:
        serifsize = random.randint(5, 30)
        e_turtle.up()
        e_turtle.goto(start[0], start[1])
        e_turtle.seth(0)
        e_turtle.goto(start[0], start[1]-height)
        e_turtle.down()
        e_turtle.back(serifsize // 2)
        e_turtle.up()
        e_turtle.goto(start[0], start[1])
        e_turtle.seth(0)
        e_turtle.down()
        e_turtle.back(serifsize // 2)
        e_turtle.up()
        e_turtle.goto(start[0] + width, start[1])
        e_turtle.left(90)
        e_turtle.forward(serifsize // 2)
        e_turtle.down()
        e_turtle.back(serifsize)
        e_turtle.up()
        e_turtle.goto(start[0] + mid_w, start[1] - mid_h)
        e_turtle.forward(serifsize // 2)
        e_turtle.down()
        e_turtle.back(serifsize)
        e_turtle.up()
        e_turtle.goto(start[0] + width, start[1] - height)
        e_turtle.forward(serifsize // 2)
        e_turtle.down()
        e_turtle.back(serifsize)


def drawF(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    f_turtle = turtle.Turtle()
    f_turtle.speed(10)
    # f_turtle.shape("turtle")
    f_turtle.ht()
    f_turtle.pensize(pensize)
    f_turtle.up()
    f_turtle.setpos(start[0], start[1] - height)
    f_turtle.down()
    f_turtle.goto(start[0], start[1])
    f_turtle.goto(start[0] + width, start[1])
    f_turtle.up()
    mid_h = random.randint(10, height // 2)
    mid_w = random.randint(width // 2, width)
    f_turtle.goto(start[0] + mid_w, start[1] - mid_h)
    f_turtle.down()
    f_turtle.back(random.randint(0, width))
    if serifs:
        serifsize = random.randint(5, 30)
        f_turtle.up()
        f_turtle.goto(start[0], start[1])
        f_turtle.seth(0)
        f_turtle.goto(start[0], start[1]-height)
        f_turtle.down()
        f_turtle.back(serifsize // 2)
        f_turtle.up()
        f_turtle.goto(start[0], start[1])
        f_turtle.seth(0)
        f_turtle.down()
        f_turtle.back(serifsize // 2)
        f_turtle.up()
        f_turtle.goto(start[0] + width, start[1])
        f_turtle.left(90)
        f_turtle.forward(serifsize // 2)
        f_turtle.down()
        f_turtle.back(serifsize)
        f_turtle.up()
        f_turtle.goto(start[0] + mid_w, start[1] - mid_h)
        f_turtle.forward(serifsize // 2)
        f_turtle.down()
        f_turtle.back(serifsize)


def drawG(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) -> None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    g_turtle = turtle.Turtle()
    g_turtle.speed(10)
    # g_turtle.shape("turtle)
    g_turtle.ht()
    g_turtle.pensize(pensize)
    g_turtle.up()
    posx, posy = 0, 0
    for i in range(0, 180):
        posx += cos(i * pi / 180) * width / 58
        posy += sin(i * pi / 180) * height / 114
        g_turtle.goto((start[0] + width) - posx, start[1] - posy)
        g_turtle.down()
    g_turtle.up()
    g_turtle.goto(start[0] + width, start[1] - height)
    g_turtle.down()
    g_turtle.seth(90)
    g_turtle.forward(random.randint(height // 4, height // 2))
    g_turtle.seth(180)
    g_turtle.up()
    g_len = random.randint(width // 8, width // 4)
    g_turtle.forward(g_len // 2)
    g_turtle.down()
    g_turtle.back(g_len)
    g_turtle.up()
    if serifs:
        g_turtle.goto(start[0] + width, start[1])
        serifsize = random.randint(5, 20)
        g_turtle.seth(270)
        g_turtle.forward(serifsize // 2)
        g_turtle.down()
        g_turtle.back(serifsize)


def drawH(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    h_turtle = turtle.Turtle()
    h_turtle.speed(10)
    # h_turtle.shape("turtle")
    h_turtle.ht()
    h_turtle.pensize(pensize)
    h_turtle.up()
    h_turtle.setpos(start[0], start[1] - height)
    h_turtle.down()
    h_turtle.goto(start[0], start[1])
    h_turtle.up()
    h_turtle.goto(start[0] + width, start[1])
    h_turtle.down()
    h_turtle.goto(start[0] + width, start[1] - height)
    h_turtle.up()
    midpoint = random.randint(10, height)
    h_turtle.goto(start[0] + (width // 2), start[1] - midpoint)
    cross = random.randint(width // 2, width)
    h_turtle.forward(cross // 2)
    h_turtle.down()
    h_turtle.back(cross)
    if serifs:
        serifsize = random.randint(5, 30)
        h_turtle.up()
        h_turtle.goto(start[0], start[1])
        h_turtle.seth(0)
        h_turtle.forward(serifsize // 2)
        h_turtle.down()
        h_turtle.back(serifsize)
        h_turtle.up()
        h_turtle.goto(start[0] + width, start[1])
        h_turtle.forward(serifsize // 2)
        h_turtle.down()
        h_turtle.back(serifsize)
        h_turtle.up()
        h_turtle.goto(start[0] + width, start[1] - height)
        h_turtle.forward(serifsize // 2)
        h_turtle.down()
        h_turtle.back(serifsize)
        h_turtle.up()
        h_turtle.goto(start[0], start[1] - height)
        h_turtle.forward(serifsize // 2)
        h_turtle.down()
        h_turtle.back(serifsize)


def drawI(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    i_turtle = turtle.Turtle()
    i_turtle.speed(10)
    # i_turtle.shape("turtle")
    i_turtle.ht()
    i_turtle.pensize(pensize)
    i_turtle.up()
    pos = random.randint(0, width)
    i_turtle.goto(start[0] + pos, start[1] - height)
    i_turtle.down()
    i_turtle.goto(start[0] + pos, start[1])
    if serifs:
        serifsize = random.randint(5, 30)
        i_turtle.up()
        i_turtle.seth(0)
        i_turtle.goto(start[0] + pos, start[1] - height)
        i_turtle.forward(serifsize // 2)
        i_turtle.down()
        i_turtle.back(serifsize)
        i_turtle.up()
        i_turtle.goto(start[0] + pos, start[1])
        i_turtle.forward(serifsize // 2)
        i_turtle.down()
        i_turtle.back(serifsize)


def drawJ(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    j_turtle = turtle.Turtle()
    j_turtle.speed(10)
    # j_turtle.shape("turtle")
    j_turtle.ht()
    j_turtle.pensize(pensize)
    j_turtle.up()
    j_turtle.goto(start[0] + width, start[1])
    radius = width / 2
    j_turtle.down()
    j_turtle.goto(start[0] + width, start[1] - (height - radius))
    j_turtle.up()
    j_turtle.goto(start[0], start[1] - (height - radius))
    j_turtle.down()
    j_turtle.seth(270)
    j_turtle.circle(radius, 180)
    if serifs:
        serifsize = random.randint(5, 30)
        j_turtle.up()
        j_turtle.goto(start[0] + width, start[1])
        j_turtle.seth(0)
        j_turtle.forward(serifsize // 2)
        j_turtle.down()
        j_turtle.back(serifsize)


def drawK(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    k_turtle = turtle.Turtle()
    k_turtle.speed(10)
    # k_turtle.shape("turtle")
    k_turtle.ht()
    k_turtle.pensize(pensize)
    k_turtle.up()
    k_turtle.goto(start[0], start[1] - height)
    k_turtle.down()
    k_turtle.goto(start[0], start[1])
    k_turtle.up()
    mid_long = random.randint(10, height)
    k_turtle.goto(start[0], start[1] - mid_long)
    k_turtle.down()
    k_turtle.goto(start[0] + width, start[1])
    k_turtle.up()
    k_turtle.goto(start[0], start[1] - mid_long)
    k_turtle.down()
    k_turtle.goto(start[0] + width, start[1] - height)
    if serifs:
        serifsize = random.randint(5, 30)
        k_turtle.up()
        k_turtle.seth(0)
        k_turtle.goto(start[0], start[1])
        k_turtle.forward(serifsize // 2)
        k_turtle.down()
        k_turtle.back(serifsize)
        k_turtle.up()
        k_turtle.goto(start[0] + width, start[1])
        k_turtle.forward(serifsize // 2)
        k_turtle.down()
        k_turtle.back(serifsize)
        k_turtle.up()
        k_turtle.goto(start[0] + width, start[1] - height)
        k_turtle.forward(serifsize // 2)
        k_turtle.down()
        k_turtle.back(serifsize)
        k_turtle.up()
        k_turtle.goto(start[0], start[1] - height)
        k_turtle.forward(serifsize // 2)
        k_turtle.down()
        k_turtle.back(serifsize)


def drawL(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    l_turtle = turtle.Turtle()
    l_turtle.speed(10)
    # l_turtle.shape("turtle")
    l_turtle.ht()
    l_turtle.pensize(pensize)
    l_turtle.up()
    l_turtle.goto(start[0], start[1])
    l_turtle.down()
    l_turtle.goto(start[0], start[1] - height)
    l_turtle.goto(start[0] + width, start[1] - height)
    if serifs:
        serifsize = random.randint(5, 30)
        l_turtle.up()
        l_turtle.seth(0)
        l_turtle.goto(start[0], start[1])
        l_turtle.forward(serifsize // 2)
        l_turtle.down()
        l_turtle.back(serifsize)
        l_turtle.up()
        l_turtle.goto(start[0] + width, start[1] - height)
        l_turtle.seth(90)
        l_turtle.down()
        l_turtle.forward(serifsize // 2)


def drawM(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    m_turtle = turtle.Turtle()
    m_turtle.speed(10)
    # m_turtle.shape("turtle")
    m_turtle.ht()
    m_turtle.pensize(pensize)
    m_turtle.up()
    m_turtle.goto(start[0], start[1] - height)
    m_turtle.down()
    m_turtle.goto(start[0], start[1])
    midpoint = random.randint(width // 2, width)
    m_turtle.goto(start[0] + midpoint, start[1] - midpoint)
    m_turtle.goto(start[0] + width, start[1])
    m_turtle.goto(start[0] + width, start[1] - height)
    if serifs:
        serifsize = random.randint(5, 30)
        m_turtle.up()
        m_turtle.seth(0)
        m_turtle.goto(start[0], start[1])
        m_turtle.forward(serifsize // 2)
        m_turtle.down()
        m_turtle.back(serifsize)
        m_turtle.up()
        m_turtle.goto(start[0] + width, start[1])
        m_turtle.forward(serifsize // 2)
        m_turtle.down()
        m_turtle.back(serifsize)
        m_turtle.up()
        m_turtle.goto(start[0] + width, start[1] - height)
        m_turtle.forward(serifsize // 2)
        m_turtle.down()
        m_turtle.back(serifsize)
        m_turtle.up()
        m_turtle.goto(start[0], start[1] - height)
        m_turtle.forward(serifsize // 2)
        m_turtle.down()
        m_turtle.back(serifsize)


def drawN(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    n_turtle = turtle.Turtle()
    n_turtle.speed(10)
    # n_turtle.shape("turtle")
    n_turtle.ht()
    n_turtle.pensize(pensize)
    n_turtle.up()
    n_turtle.goto(start[0], start[1] - height)
    n_turtle.down()
    n_turtle.goto(start[0], start[1])
    n_turtle.goto(start[0] + width, start[1] - height)
    n_turtle.goto(start[0] + width, start[1])
    if serifs:
        serifsize = random.randint(5, 30)
        n_turtle.up()
        n_turtle.seth(0)
        n_turtle.goto(start[0], start[1])
        n_turtle.forward(serifsize // 2)
        n_turtle.down()
        n_turtle.back(serifsize)
        n_turtle.up()
        n_turtle.goto(start[0] + width, start[1])
        n_turtle.forward(serifsize // 2)
        n_turtle.down()
        n_turtle.back(serifsize)
        n_turtle.up()
        n_turtle.goto(start[0] + width, start[1] - height)
        n_turtle.forward(serifsize // 2)
        n_turtle.down()
        n_turtle.back(serifsize)
        n_turtle.up()
        n_turtle.goto(start[0], start[1] - height)
        n_turtle.forward(serifsize // 2)
        n_turtle.down()
        n_turtle.back(serifsize)


def drawO(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) -> None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    o_turtle = turtle.Turtle()
    o_turtle.speed(10)
    # o_turtle.shape("turtle)
    o_turtle.ht()
    o_turtle.pensize(pensize)
    o_turtle.up()
    posx, posy = 0, 0
    if serifs:
        posx += 0
    for i in range(0, 360):
        posx += cos(i * pi / 180) * width / 120
        posy += sin(i * pi / 180) * height / 114
        o_turtle.goto((start[0] + (width / 2)) - posx, start[1] - posy)
        o_turtle.down()
    o_turtle.up()


def drawP(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    p_turtle = turtle.Turtle()
    p_turtle.speed(10)
    # p_turtle.shape("turtle")
    p_turtle.ht()
    p_turtle.pensize(pensize)
    p_turtle.up()
    p_turtle.setpos(start[0], start[1] - height)
    p_turtle.down()
    p_turtle.goto(start[0], start[1])
    p_turtle.seth(90)
    p_turtle.goto(start[0] + (width / 2), start[1])
    p_turtle.seth(-180)
    midy_top = random.randint(10, height)
    r1 = midy_top // 2
    p_turtle.circle(r1, -180)
    p_turtle.seth(-180)
    p_turtle.goto(start[0], start[1] - midy_top)
    if serifs:
        serifsize = random.randint(5, 30)
        p_turtle.up()
        p_turtle.goto(start[0], start[1])
        p_turtle.seth(0)
        p_turtle.goto(start[0], start[1]-height)
        p_turtle.forward(serifsize // 2)
        p_turtle.down()
        p_turtle.back(serifsize)
        p_turtle.up()
        p_turtle.goto(start[0], start[1])
        p_turtle.down()
        p_turtle.back(serifsize // 2)


def drawQ(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    q_turtle = turtle.Turtle()
    q_turtle.speed(10)
    # q_turtle.shape("turtle)
    q_turtle.ht()
    q_turtle.pensize(pensize)
    q_turtle.up()
    posx, posy = 0, 0
    if serifs:
        posx += 0
    for i in range(0, 360):
        posx += cos(i * pi / 180) * width / 120
        posy += sin(i * pi / 180) * height / 114
        q_turtle.goto((start[0] + (width / 2)) - posx, start[1] - posy)
        q_turtle.down()
    q_turtle.up()
    mid_x = start[0] + random.randint(width // 2, width)
    mid_y = start[1] - random.randint(height // 2, height)
    q_turtle.goto(mid_x, mid_y)
    q_turtle.down()
    q_turtle.seth(270)
    q_turtle.down()
    q_turtle.left(random.randint(0, 90))
    q_turtle.forward(random.randint(10, width // 2))


def drawR(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    r_turtle = turtle.Turtle()
    r_turtle.speed(10)
    # r_turtle.shape("turtle")
    r_turtle.ht()
    r_turtle.pensize(pensize)
    r_turtle.up()
    r_turtle.setpos(start[0], start[1] - height)
    r_turtle.down()
    r_turtle.goto(start[0], start[1])
    r_turtle.seth(90)
    r_turtle.goto(start[0] + (width / 2), start[1])
    r_turtle.seth(-180)
    midy_top = random.randint(10, height)
    r1 = midy_top // 2
    r_turtle.circle(r1, -180)
    r_turtle.seth(-180)
    r_turtle.goto(start[0], start[1] - midy_top)
    r_turtle.up()
    r_turtle.goto(start[0], start[1] - midy_top)
    r_turtle.down()
    r_turtle.goto(start[0] + width, start[1] - height)
    if serifs:
        serifsize = random.randint(5, 30)
        r_turtle.up()
        r_turtle.goto(start[0], start[1])
        r_turtle.seth(0)
        r_turtle.goto(start[0], start[1]-height)
        r_turtle.forward(serifsize // 2)
        r_turtle.down()
        r_turtle.back(serifsize)
        r_turtle.up()
        r_turtle.goto(start[0], start[1])
        r_turtle.down()
        r_turtle.back(serifsize // 2)
        r_turtle.up()
        r_turtle.goto(start[0] + width, start[1] - height)
        r_turtle.forward(serifsize // 2)
        r_turtle.down()
        r_turtle.back(serifsize)


def drawS(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) -> None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    s_turtle = turtle.Turtle()
    s_turtle.speed(10)
    # s_turtle.shape("turtle)
    s_turtle.ht()
    s_turtle.pensize(pensize)
    s_turtle.up()
    penx, peny, posx, posy = 0, 0, 0, 0
    for i in range(0, 150):
        posx += cos(i * pi / 180) * width / 58
        posy += sin(i * pi / 180) * (height / 2) / 110
        s_turtle.goto((start[0] + width) - posx, start[1] - posy)
        s_turtle.down()
    s_turtle.up()
    for i in range(0, 150):
        penx += cos(i * pi / 180) * width / 58
        peny += sin(i * pi / 180) * (height / 2) / 105
        s_turtle.goto((start[0]) + penx, (start[1] - height) + peny)
        s_turtle.down()
    s_turtle.up()
    if serifs:
        s_turtle.goto(start[0] + width, start[1])
        serifsize = random.randint(5, 20)
        s_turtle.seth(270)
        s_turtle.forward(serifsize // 2)
        s_turtle.down()
        s_turtle.back(serifsize)
        s_turtle.up()
        s_turtle.goto(start[0], start[1] - height)
        s_turtle.seth(270)
        s_turtle.forward(serifsize // 2)
        s_turtle.down()
        s_turtle.back(serifsize)
        s_turtle.up()


def drawT(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    t_turtle = turtle.Turtle()
    t_turtle.speed(10)
    # t_turtle.shape("turtle")
    t_turtle.ht()
    t_turtle.pensize(pensize)
    t_turtle.up()
    t_turtle.goto(start[0], start[1])
    t_turtle.down()
    t_turtle.goto(start[0] + width, start[1])
    t_turtle.up()
    t_turtle.goto(start[0] + (width // 2), start[1])
    t_turtle.down()
    t_turtle.goto(start[0] + (width // 2), start[1] - height)
    if serifs:
        serifsize = random.randint(5, 30)
        t_turtle.up()
        t_turtle.seth(0)
        t_turtle.goto(start[0] + (width // 2), start[1] - height)
        t_turtle.forward(serifsize // 2)
        t_turtle.down()
        t_turtle.back(serifsize)
        t_turtle.up()
        t_turtle.goto(start[0], start[1])
        t_turtle.seth(270)
        t_turtle.forward(serifsize // 2)
        t_turtle.down()
        t_turtle.back(serifsize)
        t_turtle.up()
        t_turtle.goto(start[0] + width, start[1])
        t_turtle.seth(270)
        t_turtle.forward(serifsize // 2)
        t_turtle.down()
        t_turtle.back(serifsize)


def drawU(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    u_turtle = turtle.Turtle()
    u_turtle.speed(10)
    # u_turtle.shape("turtle")
    u_turtle.ht()
    u_turtle.pensize(pensize)
    u_turtle.up()
    u_turtle.goto(start[0], start[1])
    radius = width / 2
    u_turtle.down()
    u_turtle.goto(start[0], start[1] - (height - radius))
    u_turtle.seth(270)
    u_turtle.circle(radius, 180)
    u_turtle.goto(start[0] + width, start[1])
    if serifs:
        serifsize = random.randint(5, 30)
        u_turtle.up()
        u_turtle.goto(start[0], start[1])
        u_turtle.seth(0)
        u_turtle.forward(serifsize // 2)
        u_turtle.down()
        u_turtle.back(serifsize)
        u_turtle.up()
        u_turtle.goto(start[0] + width, start[1])
        u_turtle.forward(serifsize // 2)
        u_turtle.down()
        u_turtle.back(serifsize)


def drawV(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    v_turtle = turtle.Turtle()
    v_turtle.speed(10)
    # v_turtle.shape("turtle")
    v_turtle.ht()
    v_turtle.pensize(pensize)
    v_turtle.up()
    midpoint = random.randint(0, width)
    v_turtle.goto(start[0], start[1])
    v_turtle.down()
    v_turtle.goto(start[0] + midpoint, start[1] - height)
    v_turtle.goto(start[0] + width, start[1])
    if serifs:
        serifsize = random.randint(5, 30)
        v_turtle.up()
        v_turtle.seth(0)
        v_turtle.goto(start[0], start[1])
        v_turtle.forward(serifsize // 2)
        v_turtle.down()
        v_turtle.back(serifsize)
        v_turtle.up()
        v_turtle.goto(start[0] + width, start[1])
        v_turtle.forward(serifsize // 2)
        v_turtle.down()
        v_turtle.back(serifsize)


def drawW(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    w_turtle = turtle.Turtle()
    w_turtle.speed(10)
    # w_turtle.shape("turtle")
    w_turtle.ht()
    w_turtle.pensize(pensize)
    w_turtle.up()
    midpoint_1 = start[0] + random.randint(0, width // 2)
    midpoint_2 = start[0] + random.randint(width // 2, width)
    w_turtle.goto(start[0], start[1])
    w_turtle.down()
    w_turtle.goto(midpoint_1, start[1] - height)
    w_turtle.goto(start[0] + random.randint(10, width // 2), start[1])
    w_turtle.goto(midpoint_2, start[1] - height)
    w_turtle.goto(start[0] + width, start[1])
    if serifs:
        serifsize = random.randint(5, 30)
        w_turtle.up()
        w_turtle.seth(0)
        w_turtle.goto(start[0], start[1])
        w_turtle.forward(serifsize // 2)
        w_turtle.down()
        w_turtle.back(serifsize)
        w_turtle.up()
        w_turtle.goto(start[0] + width, start[1])
        w_turtle.forward(serifsize // 2)
        w_turtle.down()
        w_turtle.back(serifsize)


def drawX(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    x_turtle = turtle.Turtle()
    x_turtle.speed(10)
    # x_turtle.shape("turtle")
    x_turtle.ht()
    x_turtle.pensize(pensize)
    x_turtle.up()
    x_turtle.goto(start[0], start[1])
    x_turtle.down()
    x_turtle.goto(start[0] + width, start[1] - height)
    x_turtle.up()
    x_turtle.goto(start[0] + width, start[1])
    x_turtle.down()
    x_turtle.goto(start[0], start[1] - height)
    if serifs:
        serifsize = random.randint(5, 30)
        x_turtle.up()
        x_turtle.seth(0)
        x_turtle.goto(start[0], start[1])
        x_turtle.forward(serifsize // 2)
        x_turtle.down()
        x_turtle.back(serifsize)
        x_turtle.up()
        x_turtle.goto(start[0] + width, start[1])
        x_turtle.forward(serifsize // 2)
        x_turtle.down()
        x_turtle.back(serifsize)
        x_turtle.up()
        x_turtle.goto(start[0] + width, start[1] - height)
        x_turtle.forward(serifsize // 2)
        x_turtle.down()
        x_turtle.back(serifsize)
        x_turtle.up()
        x_turtle.goto(start[0], start[1] - height)
        x_turtle.forward(serifsize // 2)
        x_turtle.down()
        x_turtle.back(serifsize)


def drawY(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    y_turtle = turtle.Turtle()
    y_turtle.speed(10)
    # y_turtle.shape("turtle")
    y_turtle.ht()
    y_turtle.pensize(pensize)
    y_turtle.up()
    mid_w = random.randint(0, width)
    mid_h = random.randint(0, height)
    y_turtle.goto(start[0], start[1])
    y_turtle.down()
    y_turtle.goto(start[0] + mid_w, start[1] - mid_h)
    y_turtle.goto(start[0] + width, start[1])
    y_turtle.up()
    y_turtle.goto(start[0] + mid_w, start[1] - mid_h)
    y_turtle.down()
    y_turtle.goto(start[0] + mid_w, start[1] - height)
    if serifs:
        serifsize = random.randint(5, 30)
        y_turtle.up()
        y_turtle.seth(0)
        y_turtle.goto(start[0], start[1])
        y_turtle.forward(serifsize // 2)
        y_turtle.down()
        y_turtle.back(serifsize)
        y_turtle.up()
        y_turtle.goto(start[0] + width, start[1])
        y_turtle.forward(serifsize // 2)
        y_turtle.down()
        y_turtle.back(serifsize)
        y_turtle.up()
        y_turtle.goto(start[0] + mid_w, start[1] - height)
        y_turtle.forward(serifsize // 2)
        y_turtle.down()
        y_turtle.back(serifsize)


def drawZ(width, height, start, serifs, penbool, boxgeneration):
    # type: (int, int, list, bool, bool, bool) ->  None
    if boxgeneration:
        BoxGeneration(width, height, start)
    if penbool:
        pensize = random.randint(0, 10)
    else:
        pensize = 3
    z_turtle = turtle.Turtle()
    z_turtle.speed(10)
    # z_turtle.shape("turtle")
    z_turtle.ht()
    z_turtle.pensize(pensize)
    z_turtle.up()
    z_turtle.goto(start[0], start[1])
    z_turtle.down()
    z_turtle.goto(start[0] + width, start[1])
    z_turtle.goto(start[0], start[1] - height)
    z_turtle.goto(start[0] + width, start[1] - height)
    if serifs:
        serifsize = random.randint(5, 30)
        z_turtle.up()
        z_turtle.seth(0)
        z_turtle.goto(start[0], start[1])
        z_turtle.seth(270)
        z_turtle.down()
        z_turtle.forward(serifsize // 2)
        z_turtle.up()
        z_turtle.goto(start[0] + width, start[1] - height)
        z_turtle.seth(90)
        z_turtle.down()
        z_turtle.forward(serifsize // 2)


def main():
    count = 0
    serif_bool = True
    pen_bool = False
    Box_bool = True
    box_size_bool = False

    para_dict = ["test", "continue"]

    print("\nRandom Font Generator\n")
    parameters = input("Boolean Parameters? Test/Continue: ")
    parameters = parameters.strip()
    if parameters.lower() not in para_dict:
        print("\nInvalid Input")
        parameters = input("Boolean Parameters? Test/Continue: ")
        parameters = parameters.strip()

    if parameters.lower() == "test":
        if box_size_bool:
            w, h = random.randint(20, 100), random.randint(20, 100)
        else:
            w, h = 80, 80
        start = [-100, 100]
        drawO(w, h, start, serif_bool, pen_bool, Box_bool)
    elif parameters.lower() == "continue":
        serifs = input("\nRanodmly Generate Seifs? Y/N: ")
        pen = input("\nRandomly Generate Pensize? Y/N: ")
        boxes = input("\nGenerate Boxes? Y/N: ")
        box_size = input("\nGenerate Randomly Sized Boxes? Y/N: ")
        sentence = input("\nInput sentence? Y/N: ")

        if serifs.strip().lower() == 'y':
            serif_bool = True
        else:
            serif_bool = False
        if pen.strip().lower() == 'y':
            pen_bool = True
        else:
            pen_bool = False
        if boxes.strip().lower() == 'y':
            Box_bool = True
        else:
            Box_bool = False
        if box_size.lower() == 'y':
            box_size_bool = True
        else:
            box_size_bool = False

        if sentence.strip().lower() == 'y':
            word = input("Input Sentence: ")
            print("\n")
            for char in word:
                x = -275 + (100 * count)
                y = 275
                start_spot = [x, y]
                if char == ' ':
                    count += 1
                if char.lower() == 'a':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawA(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'b':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawB(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'c':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawC(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'd':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawD(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'e':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawE(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'f':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawF(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'g':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawG(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'h':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawH(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'i':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawI(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'j':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawJ(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'k':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawK(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'l':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawL(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'm':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawM(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'n':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawN(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'o':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawO(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'p':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawP(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'q':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawQ(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'r':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawR(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 's':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawS(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 't':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawT(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'u':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawU(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'v':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawV(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'w':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawW(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'x':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawX(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'y':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawY(w, h, start_spot, serif_bool, pen_bool, Box_bool)
                if char.lower() == 'z':
                    count += 1
                    if box_size_bool:
                        w, h = random.randint(20, 100), random.randint(20, 100)
                    else:
                        w, h = 40, 40
                    drawZ(w, h, start_spot, serif_bool, pen_bool, Box_bool)
        else:
            if box_size_bool:
                w, h = random.randint(20, 100), random.randint(20, 100)
            else:
                w, h = 80, 80
            start_spot = [-100, 100]
            letter = input("Input letter: ")
            if letter.lower() == 'a':
                drawA(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'b':
                drawB(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'c':
                drawC(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'd':
                drawD(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'e':
                drawE(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'f':
                drawF(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'g':
                drawG(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'h':
                drawH(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'i':
                drawI(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'j':
                drawJ(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'k':
                drawK(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'l':
                drawL(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'm':
                drawM(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'n':
                drawN(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'o':
                drawO(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'p':
                drawP(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'q':
                drawQ(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'r':
                drawR(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 's':
                drawS(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 't':
                drawT(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'u':
                drawU(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'v':
                drawV(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'w':
                drawW(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'x':
                drawX(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'y':
                drawY(w, h, start_spot, serif_bool, pen_bool, Box_bool)
            if letter.lower() == 'z':
                drawZ(w, h, start_spot, serif_bool, pen_bool, Box_bool)


main()

cv = turtle.getcanvas()
cv.postscript(file="Z.ps", colormode='color')


turtle.Screen().exitonclick()
