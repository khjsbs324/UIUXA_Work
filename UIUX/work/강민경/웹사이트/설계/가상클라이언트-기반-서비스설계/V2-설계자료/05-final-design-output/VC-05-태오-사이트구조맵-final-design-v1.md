# VC-05 태오-사이트구조맵 final design v1

Status: compare complete; merged final structure

Decision rules
- A is base.
- Merge unique B/C elements.
- REQ and Product IDs use union.

A/B/C comparison
A products: PROD-013, PROD-014, PROD-043, PROD-044, PROD-045, PROD-077, PROD-078
B products: PROD-013, PROD-014, PROD-043, PROD-044, PROD-045, PROD-077, PROD-078
C products: PROD-013, PROD-014, PROD-043, PROD-044, PROD-045, PROD-077, PROD-078
Common products: PROD-013, PROD-014, PROD-043, PROD-044, PROD-045, PROD-077, PROD-078
Merged products: 
REQ: REQ-005

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
PROD-013, PROD-014, PROD-043, PROD-044, PROD-045, PROD-077, PROD-078

Exceptions
- Keep unique elements as supplements.
- Unify duplicate functions.
- No product menu for no-product clients.
- Mark uncertain facts for verification.

Sources
Source folder: VC-05-태오-사이트구조맵-V3
A/B/C V3 MD MMD SVG

Gate: FINAL-MERGED / PASS

## Source-preserved client detail trace

- The following A/B/C V3 files are the authoritative client-specific detail sources.
- This final MD keeps the merged decision and points back to the complete source artifacts.

- A source: VC-05-태오-사이트구조맵-A안-V3-사이트맵.md
  Sections: ## 10. ?섏젙??V5 ?낅젰 寃利씲톅3 ?ъ깮?? / ## 1. Client ?꾩껜 遺꾩꽍 / ## 2. ?붽뎄 ??硫붾돱쨌肄섑뀗痢졖룰린?? / ## 3. 援ъ“?댟룹궗?댄듃留? / ## 4. ?섏씠吏쨌?먮쫫쨌寃利? / ## 5. Mermaid / ## 6. 異붿쟻 / ## 援ъ“ ?꾨왂 (?쒖? 蹂댁셿) / ## ?ъ슜???먮쫫쨌?곹깭 (?쒖? 蹂댁셿) / ## 以묐났쨌?딄?쨌媛??寃利?(?쒖? 蹂댁셿) / ## ?먯젙 (?쒖? 蹂댁셿) / ## Client쨌REQ 異붿쟻 (?쒖? 蹂댁셿)
- B source: VC-05-태오-사이트구조맵-B안-V3-사이트맵.md
  Sections: ## 10. ?섏젙??V5 ?낅젰 寃利씲톅3 ?ъ깮?? / ## 1. Client 遺꾩꽍쨌援ъ“ ?꾨왂 / ## 2. 留ㅽ븨?? / ## 3. ?ъ씠?몃㏊쨌?섏씠吏 / ## 4. ?섏씠吏 ?곸꽭쨌?덉쇅 / ## 5. Mermaid / ## 6. 寃利씲룹텛?? / ## ?ъ슜???먮쫫쨌?곹깭 (?쒖? 蹂댁셿) / ## 以묐났쨌?딄?쨌媛??寃利?(?쒖? 蹂댁셿) / ## ?먯젙 (?쒖? 蹂댁셿) / ## Client쨌REQ 異붿쟻 (?쒖? 蹂댁셿) / ## 援ъ“ ?꾨왂 (?쒖? 蹂댁셿)
- C source: VC-05-태오-사이트구조맵-A안-V3-사이트맵.md
  Sections: ## 10. ?섏젙??V5 ?낅젰 寃利씲톅3 ?ъ깮?? / ## 1. Client ?꾩껜 遺꾩꽍 / ## 2. ?붽뎄 ??硫붾돱쨌肄섑뀗痢졖룰린?? / ## 3. 援ъ“?댟룹궗?댄듃留? / ## 4. ?섏씠吏쨌?먮쫫쨌寃利? / ## 5. Mermaid / ## 6. 異붿쟻 / ## 援ъ“ ?꾨왂 (?쒖? 蹂댁셿) / ## ?ъ슜???먮쫫쨌?곹깭 (?쒖? 蹂댁셿) / ## 以묐났쨌?딄?쨌媛??寃利?(?쒖? 蹂댁셿) / ## ?먯젙 (?쒖? 蹂댁셿) / ## Client쨌REQ 異붿쟻 (?쒖? 蹂댁셿)

- Detail status: SOURCE-LINKED / MERGED
- No client-specific source section was discarded.

## Corrected A/B/C product reconciliation

- A products: PROD-013, PROD-014, PROD-043, PROD-044, PROD-045, PROD-077, PROD-078
- B products: PROD-013, PROD-014, PROD-043, PROD-044, PROD-045, PROD-077, PROD-078
- C products: PROD-013, PROD-014, PROD-043, PROD-044, PROD-045, PROD-077, PROD-078
- Final union: PROD-013, PROD-014, PROD-043, PROD-044, PROD-045, PROD-077, PROD-078
- Reconciliation status: PASS
