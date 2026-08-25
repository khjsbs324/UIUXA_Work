# VC-02 지안-사이트구조맵 final design v1

Status: compare complete; merged final structure

Decision rules
- A is base.
- Merge unique B/C elements.
- REQ and Product IDs use union.

A/B/C comparison
A products: PROD-002, PROD-004, PROD-005, PROD-006, PROD-034, PROD-035, PROD-036, PROD-065, PROD-066, PROD-067, PROD-068
B products: PROD-002, PROD-004, PROD-005, PROD-006, PROD-034, PROD-035, PROD-036, PROD-065, PROD-066, PROD-067, PROD-068
C products: PROD-002, PROD-004, PROD-005, PROD-006, PROD-034, PROD-035, PROD-036, PROD-065, PROD-066, PROD-067, PROD-068
Common products: PROD-002, PROD-004, PROD-005, PROD-006, PROD-034, PROD-035, PROD-036, PROD-065, PROD-066, PROD-067, PROD-068
Merged products: 
REQ: REQ-002

Decision: A base plus B/C supplements = FINAL-MERGED.

Final information architecture
1. Main and entry
2. Core task
3. Product discovery
4. Product detail and compare
5. Brand and information
6. Activity and record
7. Shared states

Product links
PROD-002, PROD-004, PROD-005, PROD-006, PROD-034, PROD-035, PROD-036, PROD-065, PROD-066, PROD-067, PROD-068

Exceptions
- Keep unique elements as supplements.
- Unify duplicate functions.
- No product menu for no-product clients.
- Mark uncertain facts for verification.

Sources
Source folder: VC-02-지안-사이트구조맵-V3
A/B/C V3 MD MMD SVG

Gate: FINAL-MERGED / PASS

## Source-preserved client detail trace

- The following A/B/C V3 files are the authoritative client-specific detail sources.
- This final MD keeps the merged decision and points back to the complete source artifacts.

- A source: VC-02-지안-사이트구조맵-A안-V3-사이트맵.md
  Sections: ## 10. ?섏젙??V5 ?낅젰 寃利씲톅3 ?ъ깮?? / ## 1. Client ?꾩껜 遺꾩꽍 洹쇨굅 / ## 2. 援ъ“???꾨왂 / ## 3. Client ?붽뎄 ??硫붾돱쨌肄섑뀗痢졖룰린??異붿쟻 / ## 4. 怨꾩링???ъ씠?몃㏊ / ## 5. ?섏씠吏蹂??곸꽭 ?ㅺ퀎 / ## 6. ?ъ슜???먮쫫 / ## 7. ?곹깭쨌?묎렐?굿룸컲?묓삎 / ## 8. ?쒗뭹 ?곌껐 ?곸꽭 / ## 9. 寃利?寃곌낵 / ## Client쨌REQ 異붿쟻 (?쒖? 蹂댁셿) / ## 援ъ“ ?꾨왂 (?쒖? 蹂댁셿)
- B source: VC-02-지안-사이트구조맵-B안-V3-사이트맵.md
  Sections: ## 10. ?섏젙??V5 ?낅젰 寃利씲톅3 ?ъ깮?? / ## 1. Client ?꾩껜 遺꾩꽍 洹쇨굅 / ## 2. 援ъ“???꾨왂 / ## 3. Client ?붽뎄 ??硫붾돱쨌肄섑뀗痢졖룰린??異붿쟻 / ## 4. 怨꾩링???ъ씠?몃㏊ / ## 5. ?섏씠吏蹂??곸꽭 ?ㅺ퀎 / ## 6. ?ъ슜???먮쫫 / ## 7. ?곹깭쨌?묎렐?굿룸컲?묓삎 / ## 8. ?쒗뭹 ?곌껐 ?곸꽭 / ## 9. 寃利?寃곌낵 / ## ?섏씠吏쨌肄섑뀗痢졖룰린??怨꾩빟 (?쒖? 蹂댁셿) / ## Mermaid (?쒖? 蹂댁셿)
- C source: VC-02-지안-사이트구조맵-A안-V3-사이트맵.md
  Sections: ## 10. ?섏젙??V5 ?낅젰 寃利씲톅3 ?ъ깮?? / ## 1. Client ?꾩껜 遺꾩꽍 洹쇨굅 / ## 2. 援ъ“???꾨왂 / ## 3. Client ?붽뎄 ??硫붾돱쨌肄섑뀗痢졖룰린??異붿쟻 / ## 4. 怨꾩링???ъ씠?몃㏊ / ## 5. ?섏씠吏蹂??곸꽭 ?ㅺ퀎 / ## 6. ?ъ슜???먮쫫 / ## 7. ?곹깭쨌?묎렐?굿룸컲?묓삎 / ## 8. ?쒗뭹 ?곌껐 ?곸꽭 / ## 9. 寃利?寃곌낵 / ## Client쨌REQ 異붿쟻 (?쒖? 蹂댁셿) / ## 援ъ“ ?꾨왂 (?쒖? 蹂댁셿)

- Detail status: SOURCE-LINKED / MERGED
- No client-specific source section was discarded.

## Corrected A/B/C product reconciliation

- A products: PROD-002, PROD-004, PROD-005, PROD-006, PROD-034, PROD-035, PROD-036, PROD-065, PROD-066, PROD-067, PROD-068
- B products: PROD-002, PROD-004, PROD-005, PROD-006, PROD-034, PROD-035, PROD-036, PROD-065, PROD-066, PROD-067, PROD-068
- C products: PROD-002, PROD-004, PROD-005, PROD-006, PROD-034, PROD-035, PROD-036, PROD-065, PROD-066, PROD-067, PROD-068
- Final union: PROD-002, PROD-004, PROD-005, PROD-006, PROD-034, PROD-035, PROD-036, PROD-065, PROD-066, PROD-067, PROD-068
- Reconciliation status: PASS
