# django-project-youtube

---

# Docker 개념 정리

## Docker란?
Docker는 애플리케이션을 컨테이너라는 가상화된 환경에서 실행할 수 있게 해주는 오픈소스 플랫폼이다.
"내 컴퓨터에서 개발한 애플리케이션을 다른 환경에서도 동일하게 실행할 수 있도록" 도와준다.

---

## Docler 구성요소

(1) Docker Client
- 사용자가 Docker와 상호작용하는 인터페이스이다.
- 명령어 입력을 통해 Docker Daemon과 통신한다.

(2) Docker Daemon
- Docker의 핵심 백그라운드 서비스로 이미지 빌드, 컨테이너 실행, 네트워크 관리 등을 처리한다.

(3) Docker Registry
- Docker 이미지를 저장하고 관리하는 공간이다.
- 대표적인 레지스트리는 Docker Hub이다.
- 사용자는 이미지를 다운로드하거나, 자신이 만든 이미지를 업로드할 수 있다.

---

## Docker Imag와 Docker Containar

### Docker Imag
- 애플리케이션과 실행에 필요한 모든 파일 라이브러리, 설정 등을 포함한 템플릿이다.
- 이미지는 실행 불가능하며 이를 기반으로 컨테이너를 생성한다.

### Docker Containar
- Docker Imag를 실행 가능한 상태로 만든 실제 환경이다.
- 컨테이너는 애플리케이션이 실행되는 독립된 공간으로, 다른 컨테이너와 격리된 상태에서도 동작한다.