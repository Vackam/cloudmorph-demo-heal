# cloudmorph-demo-heal

CloudMorph 시연용 앱. 배포하면 아래 흐름을 한 번에 보여 준다.

1. **env 질문**: `SHOP_NAME`, `ADMIN_TOKEN`이 필수라 배포 전에 대시보드가 값을 묻는다.
2. **자가치유**: Dockerfile이 `PORT=8080`을 무시하고 `5000`에 바인딩해서 첫 배포가 실패한다. healer가 규칙으로 바인딩을 고친다.
3. **동의 → PR**: Dockerfile은 저장소 코드라서 고치기 전에 계속할지 묻고, 동의하면 이 저장소에 수정 PR을 올린 뒤 재배포한다.

시연이 끝나면 PR을 닫고(머지하지 않음) 다음 시연을 위해 `main`을 고장 난 상태로 둔다.
