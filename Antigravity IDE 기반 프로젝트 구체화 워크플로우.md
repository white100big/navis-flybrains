Antigravity IDE 기반 프로젝트 구체화 워크플로우
=============================================

네, Google Antigravity IDE를 활용하면 프로젝트를 매우 빠르고 구체적으로 현실화할 수 있습니다. [1] 

Antigravity IDE는 개발자가 일일이 코드를 짜는 기존 방식과 달리, AI 에이전트가 터미널 제어, 코드 작성, 브라우저 테스트 등을 자율적으로 수행하는 에이전트 중심 개발 환경(Agentic IDE)이기 때문입니다. [2, 3] 
이 깃허브 라이브러리(navis-flybrains)를 안티그래비티 환경에 연동하여 로보틱스 프로젝트로 빌드업하는 구체적인 개발 워크플로우는 다음과 같습니다.
------------------------------

## 🛠️ Antigravity IDE 기반 프로젝트 구체화 워크플로우## 1. 에이전트에게 전공 지식 부여 (Build with Google)
안티그래비티 초기 설정 단계에서 에이전트에게 관련 지식을 미리 장착시킬 수 있습니다. [4] 

* 
* 설정 방법: IDE 설정의 Build with Google 메뉴에서 복잡한 생물학 연산 및 3D 그래픽을 다룰 수 있도록 [Science]와 [Modern Web Guidance] 항목을 체크해 줍니다. 이렇게 하면 에이전트가 뇌 데이터 변환과 가상 환경 구축에 필요한 지식을 더 정밀하게 활용합니다. [4] 
* 

## 2. 에이전트에게 개발 자동화 지시 (Planning Mode)
안티그래비티의 우측 Agent 패널(채팅창)에 자연어로 상위 목표를 던져주면, 에이전트가 스스로 구현 계획(implementation_plan.md)을 수립하고 작업을 시작합니다. [1, 4] 

* 
* 프롬프트 예시:

"https://github.com/navis-org/navis-flybrains 라이브러리를 가상환경에 설치하고, FAFB14 표준 뇌 메쉬 데이터를 추출해줘. 그리고 로봇 시뮬레이터인 MuJoCo(또는 PyBullet) 환경에 이 3D 메쉬를 불러와 초파리 형태의 로봇 강체(Rigid Body) 구조를 생성하는 파이썬 스크립트를 작성하고 실행 검증까지 마쳐줘."

* 

## 3. 자율 실행 및 환경 구성 (Execution)
명령을 받은 안티그래비티 에이전트는 사용자를 대신해 다음과 같은 복잡한 인프라 작업을 알아서 처리합니다. [1] 

* 
* 라이브러리 의존성(pip3 install flybrains navis) 설치 및 외부 바이너리 경로 관리
* 초파리 변환용 대용량 H5 데이터 및 메쉬 파일 자동 다운로드 스크립트 실행
* 로봇 물리 엔진(시뮬레이터)과 공간 좌표를 일치시키는 수학적 변환 코드 작성 [2, 5] 
* 

## 4. 결과 검증 및 피드백 (Verification & Artifacts)
에이전트는 코드를 작성한 뒤 내부 터미널이나 헤드리스 브라우저를 통해 코드가 제대로 도는지 자체 검증(Verification)을 거칩니다. [1, 6] 

* 
* 시뮬레이터 화면이나 3D 시각화 결과물은 Artifacts 뷰를 통해 시각적으로 확인할 수 있습니다.
* 만약 3D 메쉬가 깨지거나 시뮬레이터에서 오류가 나면 에이전트가 로그를 읽고 스스로 디버깅하여 코드를 수정합니다. 사용자는 완성된 결과물(아티팩트)에 피드백만 남겨주면 됩니다. [2, 6, 7] 
* 

------------------------------
## 💡 추천하는 초기 폴더 세팅 (Global Rules)
안티그래비티 IDE의 Customization > Rules 메뉴에 아래와 같은 규칙을 추가해 두면, 에이전트가 파일과 데이터를 엉키지 않게 엄격하게 분류하며 개발하므로 대규모 로보틱스 프로젝트로 확장하기 유리합니다. [4] 

- 모든 사고 과정과 답변은 한글로 작성합니다.- 프로젝트 수행 시 과학적 타당성과 재현 가능성을 최우선으로 합니다.- 아래 구조의 폴더 시스템을 강제합니다:
  /primary_data : 초파리 원시 커넥톰 및 메쉬 데이터
  /simulation_env : MuJoCo 등 로봇 시뮬레이션 환경 파일
  /controllers : 초파리 신경망 모방 로봇 제어 소스코드
  /visualizations : 3D 렌더링 이미지 및 플롯 결과물

안티그래비티 IDE를 사용하면 복잡한 생물학 좌표 변환과 로봇 물리 엔진 결합이라는 난이도 높은 작업을 AI 조수와 협업하는 형태로 아주 쉽고 빠르게 구체화할 수 있습니다. [2, 4] 
프로젝트의 첫 단추로 어떤 로봇 시뮬레이터 환경(예: MuJoCo, PyBullet, Webots 등)을 염두에 두고 계시나요? 혹은 실제 하드웨어 로봇 제어까지 고려 중이신지 알려주시면, 에이전트에게 입력할 더 정밀한 초기 프롬프트 설계를 도와드리겠습니다.

[1] [https://github.com](https://github.com/hamodywe/antigravity-mastery-handbook)
[2] [https://antigravity.google](https://antigravity.google/docs/ide/overview/)
[3] [https://www.elancer.co.kr](https://www.elancer.co.kr/blog/detail/1046)
[4] [https://wikidocs.net](https://wikidocs.net/371741)
[5] [https://github.com](https://github.com/navis-org/navis-flybrains)
[6] [https://antigravity.google](https://antigravity.google/product/antigravity-ide?authuser=31)
[7] [https://realpython.com](https://realpython.com/ref/ai-coding-tools/google-antigravity/)
