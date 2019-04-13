from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# from PPT3D.glfw import *
from win32api import GetSystemMetrics
import sys
from PPT3D.settings import Settings
from PPT3D.renderer import Renderer
from PPT3D.templates import Templates
from PIL import Image


class PPT3D:

    def __init__(self):

        # 初始化组件
        self.settings = Settings()
        # self.renderer = Renderer()
        self.templates = Templates()

        # 取得屏幕大小
        self.zoom_window = 0.5
        self.rect_screen = list(map(int, [GetSystemMetrics(0), GetSystemMetrics(1)]))
        self.rect_window = list(map(int, [self.rect_screen[0] * self.zoom_window,
                                          self.rect_screen[1] * self.zoom_window]))
        # print(self.rect_screen)

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH | GLUT_MULTISAMPLE)
        glutInitWindowSize(self.rect_window[0], self.rect_window[1])
        self.window = glutCreateWindow('Hello PyOpenGL')
        glutDisplayFunc(self.draw)
        glutIdleFunc(self.draw)
        self.glut_init(self.rect_window[0], self.rect_window[1])
        # 绕各坐标轴旋转的角度
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

        # 初始化OpenGL

    # 绘制图形
    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        # 沿z轴平移
        glTranslate(0.0, 0.0, -self.z)
        # 分别绕x,y,z轴旋转
        glRotatef(self.x, 1.0, 0.0, 0.0)
        glRotatef(self.y, 0.0, 1.0, 0.0)
        glRotatef(self.z, 0.0, 0.0, 1.0)

        # 开始绘制立方体的每个面，同时设置纹理映射
        glBindTexture(GL_TEXTURE_2D, 0)
        # 绘制四边形
        glBegin(GL_QUADS)
        # 设置纹理坐标
        glTexCoord2f(0.0, 0.0)
        # 绘制顶点
        glVertex3f(-1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glEnd()

        # 切换纹理
        glBindTexture(GL_TEXTURE_2D, 1)
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(1.0, -1.0, -1.0)
        glEnd()

        # 切换纹理
        glBindTexture(GL_TEXTURE_2D, 2)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glEnd()

        # 切换纹理
        glBindTexture(GL_TEXTURE_2D, 3)
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(1.0, -1.0, -1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glEnd()

        # 切换纹理
        glBindTexture(GL_TEXTURE_2D, 4)
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(1.0, -1.0, 1.0)
        glEnd()

        # 切换纹理
        glBindTexture(GL_TEXTURE_2D, 5)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        # 结束绘制
        glEnd()

        # 刷新屏幕，产生动画效果
        glutSwapBuffers()
        # 修改各坐标轴的旋转角度
        self.x += 0.02 * 4
        self.y += 0.03 * 4
        self.z += 0.01 * 4

        # glDisable(GLUT_MULTISAMPLE)

    # 加载纹理
    def LoadTexture(self):
        # 提前准备好的6个图片
        imgFiles = [str('img') + '.jpg' for i in range(1, 7)]
        for i in range(6):
            img = Image.open(imgFiles[i])
            width, height = img.size
            img = img.tobytes('raw', 'RGBX', 0, -1)

            glGenTextures(2)
            glBindTexture(GL_TEXTURE_2D, i)
            glTexImage2D(GL_TEXTURE_2D, 0, 4,
                         width, height, 0, GL_RGBA,
                         GL_UNSIGNED_BYTE, img)
            glTexParameterf(GL_TEXTURE_2D,
                            GL_TEXTURE_WRAP_S, GL_CLAMP)
            glTexParameterf(GL_TEXTURE_2D,
                            GL_TEXTURE_WRAP_T, GL_CLAMP)
            glTexParameterf(GL_TEXTURE_2D,
                            GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameterf(GL_TEXTURE_2D,
                            GL_TEXTURE_WRAP_T, GL_REPEAT)
            glTexParameterf(GL_TEXTURE_2D,
                            GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glTexParameterf(GL_TEXTURE_2D,
                            GL_TEXTURE_MIN_FILTER, GL_NEAREST)
            glTexEnvf(GL_TEXTURE_ENV,
                      GL_TEXTURE_ENV_MODE, GL_DECAL)

    def glut_init(self, width, height):
        print(glGetIntegerv(GL_SAMPLE_BUFFERS), glGetIntegerv(GL_SAMPLES))

        glEnable(GL_MULTISAMPLE)

        self.LoadTexture()
        glEnable(GL_TEXTURE_2D)
        glClearColor(0.5, 0.5, 0.5, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glShadeModel(GL_SMOOTH)
        # 背面剔除，消隐
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        glEnable(GL_POINT_SMOOTH)
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_POLYGON_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
        glHint(GL_POLYGON_SMOOTH_HINT, GL_FASTEST)
        glLoadIdentity()
        gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)


    # def keyboard(self, window, key, scancode, action, mods):
    #     if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
    #         glfwSetWindowShouldClose(window, 1)

    # def mainloop(self):
    #     img = Image.open('img.jpg')
    #     data = img.tobytes('raw', 'RGBX', 0, -1)
    #
    #     glGenTextures(2)
    #     glBindTexture(GL_TEXTURE_2D, 0)
    #     glTexImage2D(GL_TEXTURE_2D, 0, 4,
    #                  img.size[0], img.size[1], 0, GL_RGBA,
    #                  GL_UNSIGNED_BYTE, data)
    #     glTexParameterf(GL_TEXTURE_2D,
    #                     GL_TEXTURE_WRAP_S, GL_CLAMP)
    #     glTexParameterf(GL_TEXTURE_2D,
    #                     GL_TEXTURE_WRAP_T, GL_CLAMP)
    #     glTexParameterf(GL_TEXTURE_2D,
    #                     GL_TEXTURE_WRAP_S, GL_REPEAT)
    #     glTexParameterf(GL_TEXTURE_2D,
    #                     GL_TEXTURE_WRAP_T, GL_REPEAT)
    #     glTexParameterf(GL_TEXTURE_2D,
    #                     GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    #     glTexParameterf(GL_TEXTURE_2D,
    #                     GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    #     glTexEnvf(GL_TEXTURE_ENV,
    #               GL_TEXTURE_ENV_MODE, GL_DECAL)
    #
    #     while not glfwWindowShouldClose(self.window):
    #         # Render here
    #         width, height = glfwGetFramebufferSize(self.window)
    #         ratio = width / float(height)
    #         glViewport(0, 0, width, height)
    #         gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)
    #         glClear(GL_COLOR_BUFFER_BIT)
    #         glMatrixMode(GL_PROJECTION)
    #         glLoadIdentity()
    #         glOrtho(-ratio, ratio, -1, 1, 1, -1)
    #         glMatrixMode(GL_MODELVIEW)
    #         # 回复到中心点开始绘制
    #         glLoadIdentity()
    #         glTranslate(glfwGetTime() / 10, 0, 0)
    #         # glRotatef(glfwGetTime() * 10, 0, 0, 1)
    #         # glTranslate(0, 0, glfwGetTime())
    #         glBegin(GL_TRIANGLES)
    #         glColor3f(1, 0, 0)
    #         glVertex3f(-0.6, -0.4, 0)
    #         glColor3f(0, 1, 0)
    #         glVertex3f(0.6, -0.4, 0)
    #         glColor3f(0, 0, 1)
    #         glVertex3f(0, 0.6, 0)
    #         glEnd()
    #
    #         # 切换纹理
    #         glBindTexture(GL_TEXTURE_2D, 0)
    #         glBegin(GL_QUADS)
    #         glTexCoord2f(0.0, 0.0)
    #         glVertex3f(-1.0, -1.0, -1.0)
    #         glTexCoord2f(1.0, 0.0)
    #         glVertex3f(-1.0, -1.0, 1.0)
    #         glTexCoord2f(1.0, 1.0)
    #         glVertex3f(-1.0, 1.0, 1.0)
    #         glTexCoord2f(0.0, 1.0)
    #         glVertex3f(-1.0, 1.0, -1.0)
    #         # 结束绘制
    #         glEnd()
    #
    #         # 刷新屏幕
    #         glfwSwapBuffers(self.window)
    #
    #         # Poll for and process events
    #         glfwPollEvents()
    #
    #     # 释放GLFW的内存
    #     glfwTerminate()

    def mainloop(self):
        glutMainLoop()