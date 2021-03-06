# 기말 프로젝트  

## 1. 게임 소개
 * 제목: 슈퍼마리오 메이커
 
 **1. 원 게임의 대한 정보 및 스크린샷**
 
 <a href="#"><img src="http://img.tf.co.kr/article/home/2015/10/01/201548081443658722.jpg" width="600px" alt="sample image"></a> 
 
 슈퍼마리오 메이커는 닌텐도 Wii U 전용으로 발매한 슈퍼 마리오 시리즈의 편집툴이자 게임입니다.  
 스테이지를 직접 만들어 플레이하고 이를 공유할 수 있고, 다른 사람이 만든 스테이지를 플레이할 수도 있습니다.  
 저는 스테이지를 직접만드는 툴과 플레이 할 수 있도록 인게임 씬을 만들 계획입니다.
 
 **2. 게임의 목적, 방법 등 간단한 설명**
 
 툴을 이용하여 게임의 요소들을 직접 배치하여 맵을 제작하고, 만들어진 맵을 직접 플레이하는 것이 목적입니다.
 
 
 툴: 마우스를 이용하여 게임의 블럭이나 몬스터들을 직접 배치합니다.
 
 게임씬: 만들어진 맵을 직접 플레이합니다. 조작키: 상하좌우키, 점프:A, 달리기:S
 
 
 ## 2. GameState (Scene) 의 수 및 각각의 이름
 
 * GameState(Scene)의 수: 5개
 * 게임 타이틀, 메뉴, 인게임, 툴, 게임 클리어/게임 오버
 
 
 ## 3. 각 GameState 별 다음 항목
 **1. 게임 타이틀**
 - 스페이스키로 다음 씬으로 넘어갈수 있는 게임 타이틀입니다.
 - 마우스 입력은 받지않고 스페이스바를 눌러 다음 씬으로 넘어갑니다. 
 
 **2. 메뉴**  
 - 게임을 플레이 할 수있는 인게임과 툴을 이용할 수 있는 툴 씬으로 넘어갈수 있는 버튼이 있습니다.
 - 키보드 입력은 없고 마우스 입력으로 버튼을 클릭하여 해당 씬으로 이동합니다.  
 
 **3. 인게임**
 - 슈퍼마리오의 인게임 씬입니다.
 - 툴에서 제작한 맵을 토대로 블록과 몬스터 파이프 등이 화면에 출력됩니다.
 - 키보드 입력만 받으며 마우스 입력은 받지 않습니다.
 - 게임 클리어나 게임 오버시 게임 클리어/게임 오버 씬으로 이동합니다.  
 
 **4. 툴**
 - 슈퍼마리오 인게임에 사용할 맵을 제작하는 툴입니다.
 - 배치할 수 있는 블록과 몬스터등이 있습니다.
 - 키보드와 마우스 입력을 전부 받습니다.  
 
 **5. 게임 클리어/게임 오버**
 - 게임 클리어시 점수를 보여주고 게임 오버시 게임 오버라는 글자가 뜹니다.
 - 키보드 입력만 받으며 스페이스바를 입력시 메뉴 씬으로 이동합니다.
 
 ## 4. 필요한 기술  
 **1. 다른 과목에서 배운 기술**  
 - 파일 입출력, 마우스 이벤트  
 
 **2. 이 과목에서 배울것으로 기대되는 기술**  
 - 파일 입출력, 배경 스크롤, 충돌처리  
 
 **3. 다루지 않은 것 같아서 수업에 다루어  달라고 요청할 기술**  
 - 마우스 이벤트, 충돌 처리, 파일 입출력, 버튼, 사운드, 화면 전환효과(페이드인 페이드아웃)
 
 ## 5. 게임 컨셉
 - 게임의 맵을 직접 제작하여 플레이 한다.
 - 배치 할 수 있는 요소들을 최대한 많이 구현

 ## 6. 개발 범위
 **1. 맵 툴**
 - 기본적인 배치 요소 구현(캐릭터, 블록, 파이프, 몬스터)
 - 저장 및 불러오기
 
 **2. 캐릭터 컨트롤**
 - 방향키(상하좌우), 점프
 - 캐릭터는 좌우 방향으로만 이동
 
 **3. 캐릭터 상호작용**
 - 버섯: 캐릭터의 크기가 커지고 피격시 다시 작아짐
 - 파이프: 파이프 위에서 아래방향 입력 시 다른맵으로 이동
 - 물음표블록: 점프 하여 머리방향과 블록이 충돌 시 아이템 생성

 **4. 몬스터**
 - 굼바: 좌우 방향 이동. 벽, 파이프와 충돌 시 반대 방향으로 이동
 - 거북이: 좌우 방향 이동. 벽, 파이프와 충돌 시 반대 방향으로 이동 ,거북이의 머리를 밟으면 등껍질 상태가 되며 밀어낸 방향으로 빠르게 이동(피격 시 몬스터 킬 및 캐릭터 공격받음)
 
 **5. 게임 기능**
 - 몬스터와 피격 시 사망 및 목숨 감소
 - 툴을 이용한 다양한 맵 제작 가능
 
 **6. 사운드**
 - 점프, 캐릭터,몬스터 피격, 블록과 부딛치는 소리, 파이프 들어가는 소리, 버섯 먹는소리, 게임 배경음

 **7. 애니메이션**
 - 캐릭터: 걷기, 점프, 앉기, 버섯을 먹은 캐릭터(걷기,점프,앉기) 애니메이션
 - 몬스터: 걷기, 사망 애니메이션
 
 ## 7. 게임 실행 흐름
 
 **1. 게임 화면 구성(맵)**
 ![111](https://user-images.githubusercontent.com/66163299/95560300-0c9bcd80-0a54-11eb-84eb-85bb9ee2f867.PNG)
 
 **2. 게임 화면 구성(툴)**
 ![222](https://user-images.githubusercontent.com/66163299/95560435-3e149900-0a54-11eb-8bd3-bb2a9a7bbc4e.PNG)
 
 **3. 게임 흐름**
 ![333](https://user-images.githubusercontent.com/66163299/95560444-3fde5c80-0a54-11eb-96f6-6cf9b6bd1545.PNG)
 
 ## 8. 개발 일정
 ![22222](https://user-images.githubusercontent.com/66163299/96332678-5ca41100-10a0-11eb-82a0-f5e6d72626f7.PNG)

