# django-project-youtube

## Model 구조 => ORM

(1) User
- email
- password
- nickname
- is_business

(2) Video
- title
- description
- link
- views_count
- thumbnail
- video_file: link
- User: FK

ex) 파일(이미지, 동영상)
=> 장고에 부하가 걸림.
=> S3 Bucket(저렴, 속도가 빠름) -> 결과물: 링크

(3) Reaction
- User: FK
- Video: FK
- reaction (like, dislike, cancel) => 실제 youtube rest api

(4) Comment
- User: FK
- Video: FK
- content
- like
- dislike

(5) Subscription
- User: FK => subscriber (내가 구독한 사람)
- User: FK => subscribed_to (나를 구독한 사람)

(6) Common
- created_at
- updated_at

모델을 먼저 정의한 이유는 Django -> DB migration(테이블 구조 정의) => REST API
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

---

# CI/CD

👉 https://velog.io/@sangwoong/CICD-GitHub-Action%EC%9C%BC%EB%A1%9C-CICD-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0 👈

## CI 지속적인 통합
지속적 통합은 개발 팀이 코드를 지속적으로 통합하고 이를 자동으로 테스트하여 통합 버그를 최소화하는 프로세스를 의미합니다. 주요 특징은 다음과 같습니다:
- 코드 변경 사항이 발생 (push)할 때마다 자동으로 빌드 및 테스트를 실행합니다.
- 개발자들은 자주 코드를 통합할 수 있으며, 코드가 충돌되는 현상(conflict)을 미리 발견할 수 있습니다.
- 프로덕트 품질 관리 및 버그 발견이 빨라집니다.

## CD 지속적인 배포
지속적 배포는 지속적으로 통합된 코드를 자동으로 프로덕션 환경에 배포하는 프로세스입니다. 주요 특징은 다음과 같습니다:
- 코드 변경 사항이 테스트 및 승인(approve)을 거쳐 자동으로 프로덕션 환경에 배포(merge to main)됩니다.
- 새로운 기능과 버그 수정 사항이 실제 사용자에게 빠르게 제공됩니다.
- 사용자 피드백을 수집하고 제품을 개선하는 속도를 향상시킬 수 있습니다.

## GitHub Action
GitHub Actions은 GitHub 플랫폼에서 제공하는 자동화 및 지속적 통합/지속적 배포(CI/CD) 서비스입니다. GitHub Action을 사용하면 코드의 통합과 배포 프로세스를 자동화하여 개발 생산성을 향상시킬 수 있습니다.

👉 GitHub Action 공식문서 이동하기  https://docs.github.com/en/actions 👈

---

# PostgreSQL 장점

👉 https://bitnine.net/blog-postgresql/postgresql%EC%9D%98-%EC%9E%A5%EC%A0%90%EA%B3%BC-%EB%8B%A8%EC%A0%90/ 👈

(1) 뛰어난 확장성 
수직적 확장성은 PostgreSQL의 특징입니다. 거의 모든 맞춤형 소프트웨어 솔루션이 성장하여 데이터베이스를 확장하는 경향이 있다는 점을 고려할 때, 이 특정 옵션은 확실한 비즈니스 성장과 개발을 지원합니다.

(2) 사용자 정의 데이터 유형 지원
PostgreSQL은 기본적으로 JSON, XML, H-Store 등 다양한 데이터 유형을 지원합니다. PostgreSQL은 NoSQL 기능을 강력하게 지원하는 몇 안 되는 관계형 데이터베이스 중 하나이기 때문에 그 많은 데이터 유형을 지원하는 것입니다. 또한 사용자가 직접 데이터 유형을 정의할 수 있습니다. 소프트웨어 비즈니스 모델에 따라 더 나은 성능이나 애플리케이션의 포괄성을 위해 다양한 유형의 데이터베이스가 필요할 수 있으므로, 이 옵션을 사용하면 유연성이 향상되는 것을 확인할 수 있습니다.

(3) 쉽게 통합 가능한 서드파티 도구 
PostgreSQL DBMS는 무료 및 상용 도구에 강력한 추가 지원을 제공합니다. 여기에는 Postgres의 여러 측면을 개선하기 위한 확장 기능(extension)들이 포함됩니다. 예를 들어, ClusterControl은 SQL 및 NoSQL 오픈소스 데이터베이스를 관리하고 모니터링 및 확장에 대한 지원을 합니다. 데이터 비교 및 동기화를 보다 효과적으로 수행하려면 DB Data Directive를 사용하는 것을 권장합니다. 워크로드가 많은 데이터로 확장하려는 경우, pgBackRest 백업 및 복원 시스템이 좋은 옵션이 될 것입니다.

(4) 오픈소스 및 커뮤니티 중심 지원
PostgreSQL은 완전한 오픈소스이며 다양한 커뮤니티의 지원을 받아 완전한 에코시스템으로 자리를 잡았습니다. 소스코드가 오픈소스 라이선스를 따르기 때문에 비즈니스 요구에 따라 자유롭게 사용, 수정, 구현할 수 있습니다.
이 외에 PostgreSQL의 주목할 만한 장점을 소개합니다.
- LAMP 스택 옵션으로 웹사이트와 웹 애플리케이션을 실행
- WAL(미리 쓰기 로그)로 데이터베이스의 내결함성 향상
- 지리적 개체를 지원하므로 위치 기반 서비스 및 지리 정보 시스템을 위한 지리 공간 데이터 저장소로 사용 가능
- 사용하기 쉽기 때문에 많은 교육이 필요하지 않음
- 임베디드 및 엔터프라이즈에서 PostgreSQL을 사용할 때 간편한 유지 및 관리