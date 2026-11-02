from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    image = None  # 공 이미지는 모든 공이 같이 쓰므로 클래스 변수로 한 번만 로드

    def __init__(self, x, y, velocity):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = x, y
        self.velocity = velocity  # 양수면 오른쪽, 음수면 왼쪽으로 날아감

    def update(self):
        self.x += self.velocity
        # 화면 밖으로 나가면 게임 월드에서 제거
        if self.x < -25 or self.x > get_canvas_width() + 25:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
