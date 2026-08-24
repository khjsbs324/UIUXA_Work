import os

client_dir = r'C:\UIUX이지희\Antigravity\클라이언트 분석'

rename_map = {
    '클라이언트 분석1.md': '[클라이언트01]_차은채_WICKETA총괄디렉터_D2C안식처.md',
    '클라이언트 분석2.md': '[클라이언트02]_강이현_WICKETA_B2B이사_탕비실구독.md',
    '클라이언트 분석3.md': '[클라이언트03]_신유진_WICKETA_조향사_DIY믹솔로지.md',
    '클라이언트 분석4.md': '[클라이언트04]_백서진_WICKETA_럭셔리_프리미엄각인.md',
    '클라이언트 분석5.md': '[클라이언트05]_한지안_WICKETA_BM_제로슈가스틱.md',
    '클라이언트 분석6.md': '[클라이언트06]_윤서연_29SELECT_수석MD_감성큐레이션.md',
    '클라이언트 분석7.md': '[클라이언트07]_최하은_공간디자이너_3D가상투어.md',
    '클라이언트 분석8.md': '[클라이언트08]_임태경_부티크호텔이사_인룸티타임.md',
    '클라이언트 분석9.md': '[클라이언트09]_권명수_뷰티편집숍CEO_이너뷰티.md',
    '클라이언트 분석10.md': '[클라이언트10]_송아린_숏폼크리에이터_믹솔로지챌린지.md',
    '클라이언트 분석11.md': '[클라이언트11]_이도은_P4디자이너_비밀안식처.md',
    '클라이언트 분석12.md': '[클라이언트12]_박지후_P3IT대리_3분퀵브루ing.md',
    '클라이언트 분석13.md': '[클라이언트13]_이지민_P2대학생_오로라수색비주얼.md',
    '클라이언트 분석14.md': '[클라이언트14]_윤기준_P7개발팀장_정밀브루잉타이머.md',
    '클라이언트 분석15.md': '[클라이언트15]_서지안_P8육아대디_노동제로논알콜하이볼.md',
}

for old_name, new_name in rename_map.items():
    old_path = os.path.join(client_dir, old_name)
    new_path = os.path.join(client_dir, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f'Renamed: {old_name} -> {new_name}')
    else:
        print(f'File not found: {old_name}')

print('File renaming completed!')
