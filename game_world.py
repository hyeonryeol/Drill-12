#게임월드 리스트 초기화
#world = [] #객체들의 리스트, 빈 리스트

world = [[], [], []]

#게임월드에 객체 추가
def add_object(o, depth = 0): #depth = 0 기본값을 0으로 설정
    world[depth].append(o)

#게임월드에서 객체 제거
def remove_object(o):
    for layer in world: #모든 레이어를 순회하면서 객체를 제거
        if o in layer: #객체가 해당 레이어에 존재하면 제거
            layer.remove(o)
            return #제거 후 함수 종료
        
#게임로직
def update():
    for layer in world: #모든 레이어를 순회하면서 업데이트
        for o in layer: #해당 레이어의 모든 객체를 업데이트
            o.update()

#게임 월드 렌더링
def render():
    for layer in world: #모든 레이어를 순회하면서 렌더링
        for o in layer: #해당 레이어의 모든 객체를 렌더링
            o.draw()
    