# VC-28 수현-사이트구조맵 final design v1

Status: compare complete; merged final structure

Decision rules
- A is base.
- Merge unique B/C elements.
- REQ and Product IDs use union.

A/B/C comparison
A products: PROD-008, PROD-011, PROD-027, PROD-037, PROD-056, PROD-061, PROD-070, PROD-093
B products: PROD-008, PROD-011, PROD-027, PROD-037, PROD-056, PROD-061, PROD-070, PROD-093
C products: PROD-008, PROD-011, PROD-027, PROD-037, PROD-056, PROD-061, PROD-070, PROD-093
Common products: PROD-008, PROD-011, PROD-027, PROD-037, PROD-056, PROD-061, PROD-070, PROD-093
Merged products: 
REQ: REQ-028

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
PROD-008, PROD-011, PROD-027, PROD-037, PROD-056, PROD-061, PROD-070, PROD-093

Exceptions
- Keep unique elements as supplements.
- Unify duplicate functions.
- No product menu for no-product clients.
- Mark uncertain facts for verification.

Sources
Source folder: VC-28-수현-사이트구조맵-V3
A/B/C V3 MD MMD SVG

Gate: FINAL-MERGED / PASS

## Source-preserved client detail trace

- The following A/B/C V3 files are the authoritative client-specific detail sources.
- This final MD keeps the merged decision and points back to the complete source artifacts.

- A source: VC-28-수현-사이트구조맵-A안-V3-사이트맵.md
  Sections: ## 1. Client쨌REQ 異붿쟻 / ## 2. 援ъ“ ?꾨왂 / ## 3. ?섏씠吏쨌肄섑뀗痢졖룰린??怨꾩빟 / ## 4. ?ъ슜???먮쫫쨌?곹깭 / ## 5. 以묐났쨌?딄?쨌媛??寃利?- ?ъ쭊 移대뱶? 留λ씫 ?쇰꺼? 蹂댁“ 洹쇨굅?대ŉ OCR ?먮룞 異붿텧???꾩젣?섏? ?딅뒗?? / ## 6. Mermaid / ## 7. ?먯젙
- B source: VC-28-수현-사이트구조맵-B안-V3-사이트맵.md
  Sections: ## 1. Client쨌REQ 異붿쟻 / ## 2. 援ъ“ ?꾨왂 / ## 3. ?섏씠吏쨌肄섑뀗痢졖룰린??怨꾩빟 / ## 4. ?ъ슜???먮쫫쨌?곹깭 / ## 5. 以묐났쨌?딄?쨌媛??寃利?- 二쇱젣 ?몃뜳?ㅼ? ?쇰꺼 ?명듃媛 媛숈? ?꾩튂瑜?以묐났 二쇱옣?섏? ?딅룄濡?異쒖쿂瑜?蹂묎린?쒕떎. / ## 6. Mermaid / ## 7. ?먯젙
- C source: VC-28-수현-사이트구조맵-A안-V3-사이트맵.md
  Sections: ## 1. Client쨌REQ 異붿쟻 / ## 2. 援ъ“ ?꾨왂 / ## 3. ?섏씠吏쨌肄섑뀗痢졖룰린??怨꾩빟 / ## 4. ?ъ슜???먮쫫쨌?곹깭 / ## 5. 以묐났쨌?딄?쨌媛??寃利?- ?ъ쭊 移대뱶? 留λ씫 ?쇰꺼? 蹂댁“ 洹쇨굅?대ŉ OCR ?먮룞 異붿텧???꾩젣?섏? ?딅뒗?? / ## 6. Mermaid / ## 7. ?먯젙

- Detail status: SOURCE-LINKED / MERGED
- No client-specific source section was discarded.

## Corrected A/B/C product reconciliation

- A products: PROD-008, PROD-011, PROD-027, PROD-037, PROD-056, PROD-061, PROD-070, PROD-093
- B products: PROD-008, PROD-011, PROD-027, PROD-037, PROD-056, PROD-061, PROD-070, PROD-093
- C products: PROD-008, PROD-011, PROD-027, PROD-037, PROD-056, PROD-061, PROD-070, PROD-093
- Final union: PROD-008, PROD-011, PROD-027, PROD-037, PROD-056, PROD-061, PROD-070, PROD-093
- Reconciliation status: PASS
