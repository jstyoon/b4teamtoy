# B4 teamtoy project

---

## 팀 프로젝트 개발 환경

`Python 3.11`
`Django 4.2`
`Django Rest Framework 3.14`

---

## 팀 프로젝트 소개

> **B4games**
> 재밌는 게임을 추천 소개, 공유 하는 서비스

> 컨셉 사이트

- [Epicgames](https://store.epicgames.com/)
- [Steam](https://store.steampowered.com/)

---

## [ERD](https://www.erdcloud.com/d/7KTHFPDdfAvAcpLas)

![old](https://github.com/jstyoon/b4teamtoy/assets/103176409/9f82746e-17f4-4428-a4f2-72d3c3cd3e16)
![ERDcloud](https://github.com/jstyoon/b4teamtoy/assets/103176409/43b5d8d5-fe3e-4641-b3b3-bb6bee0e8d9c)

---

## 백엔드 이슈

프론트와 서버 배포가 완료되지 않은 관계로 추후 피드백을 반영하고 학습하기 위한 용도로 이슈를 기록했습니다

### 프로젝트 초기 설정

![0509에러1](https://github.com/jstyoon/b4teamtoy/assets/103176409/415f174b-ebba-4e60-b87d-cf830ffae1e3)
[backports.zoneinfo 0.2.1](https://pypi.org/project/backports.zoneinfo/) 개발환경을 통일하지 않고 작업 진행중 `Python 3.9`버전 미만의 환경에 설치되어 다른 버전을 사용하는 작업자와 공유 시 에러를 유발하는 헤당 package확인. 버전 통합후 해결했습니다.

> 가장 먼저 팀 개발 환경을 동일하게 합니다.

---

### 디자인 패턴

mvc 패턴으로 작성된 프로필 구현부를 serializer를 사용하여 변경 해주었습니다.

> mvc, mvt 패턴 개념을 이해하고 기능을 정의해야 합니다.
> [Difference between MVC and MVT design patterns](https://www.geeksforgeeks.org/difference-between-mvc-and-mvt-design-patterns/)

---

### 서비스 코어 계획

유저모델(User)에 판매자 계정 필드`is_seller(Boolean)`를 추가하여 유저를구분하고 회원가입을 구현했습니다. 하지만 판매자의 권한을 정의할 수 있는 shop application (`결제` or `판매`) 을 정의하지 못하고 결국 핵심기능이 서비스에 담기지 못했습니다.

> 서비스의 핵심 기능을 먼저 정의하고 기획하는 부분이 중요합니다.

---

### 모델 설계 고민

![image](https://github.com/jstyoon/b4teamtoy/assets/103176409/37a6a4f8-0789-47d2-b632-d98723692e9c)

    당신의 모델필드는 전부 사용되고 있나요?

로그인, 로그아웃, 회원 가입같은 필수 기능이 완료 되었으나, 꼭 필요한 데이터인지 고민이 필요한 시점에 관성적으로 유저모델에 여러 필드를 추가했던 문제를 알게되었습니다.

> 불필요한 데이터 필드는 삭제하였고 앞으로 모델 설계시에도 기능과 관계없는 필드는 넣지 않아야 합니다.

---

### 키 보안

dotenv 시크릿키가 없었기때문에 makemigrations,migrate 에러가 발생했습니다. dotenv같은 중요한 정보가 담긴 파일은 팀원끼리만 공유하면 됩니다.

> 팀원들 각자 시크릿키를 재발급 받을 필요없이
> 각자의 파일에 .env 파일을 만들고 시크릿키를 사용합니다

---

### 유저 모델 대체

로그인시 토큰사용, 비밀번호 암호화, 이메일 인증기능을 추가하기 위해 유저 모델을 대체하였습니다

> 참고 : [장고프로젝트 공식 문서](https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model)

---

### Git찮아도

Git은 개발자 협업도구의 표준으로 사용되며 대다수의 개발 결과물 관리 역시 Github을 통해 이뤄집니다. 원활한 협업 진행을 위해 틈틈히 Git 명령어를 공부합니다.

> 참고 : [Git찮아도 알아둬야할 Git명령어](https://velog.io/@4_21ee/TIL-27-Git%EC%B0%AE%EC%95%84%EB%8F%84-%EC%95%8C%EC%95%84%EB%91%AC%EC%95%BC%ED%95%A0-Git%EB%AA%85%EB%A0%B9%EC%96%B4)

---

### 회고

> 내용을 추가할 예정입니다

---
