# VC-15 새봄-사이트구조맵 final design v1

Status: compare complete; merged final structure

Decision rules
- A is base.
- Merge unique B/C elements.
- REQ and Product IDs use union.

A/B/C comparison
A products: PROD-025, PROD-026, PROD-055, PROD-057, PROD-093, PROD-094
B products: PROD-025, PROD-026, PROD-055, PROD-057, PROD-093, PROD-094
C products: PROD-025, PROD-026, PROD-055, PROD-057, PROD-093, PROD-094
Common products: PROD-025, PROD-026, PROD-055, PROD-057, PROD-093, PROD-094
Merged products: 
REQ: REQ-015

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
PROD-025, PROD-026, PROD-055, PROD-057, PROD-093, PROD-094

Exceptions
- Keep unique elements as supplements.
- Unify duplicate functions.
- No product menu for no-product clients.
- Mark uncertain facts for verification.

Sources
Source folder: VC-15-새봄-사이트구조맵-V3
A/B/C V3 MD MMD SVG

Gate: FINAL-MERGED / PASS

## Source-preserved client detail trace

- The following A/B/C V3 files are the authoritative client-specific detail sources.
- This final MD keeps the merged decision and points back to the complete source artifacts.

- A source: VC-15-새봄-사이트구조맵-A안-V3-사이트맵.md
  Sections: ## 1. Client쨌REQ 異붿쟻 / ## 2. 援ъ“ ?꾨왂 / ## 3. ?섏씠吏쨌肄섑뀗痢졖룰린??怨꾩빟 / ## 4. ?ъ슜???먮쫫쨌?곹깭 / ## 5. 以묐났쨌?딄?쨌媛??寃利?- ?몄쬆쨌?섍꼍 ?④낵쨌?닿뎄 ?곗닔??異쒖쿂? ?뺤씤???놁씠 ?쒖떆?섏? ?딅뒗?? / ## 6. Mermaid / ## 7. ?먯젙
- B source: VC-15-새봄-사이트구조맵-B안-V3-사이트맵.md
  Sections: ## 1. Client쨌REQ 異붿쟻 / ## 2. 援ъ“ ?꾨왂 / ## 3. ?섏씠吏쨌肄섑뀗痢졖룰린??怨꾩빟 / ## 4. ?ъ슜???먮쫫쨌?곹깭 / ## 5. 以묐났쨌?딄?쨌媛??寃利?- ?숈씪 二쇱옣???섏씠吏留덈떎 蹂듭젣?섏? ?딄퀬 ID쨌異쒖쿂濡??곌껐?쒕떎. / ## 6. Mermaid / ## 7. ?먯젙
- C source: VC-15-새봄-사이트구조맵-A안-V3-사이트맵.md
  Sections: ## 1. Client쨌REQ 異붿쟻 / ## 2. 援ъ“ ?꾨왂 / ## 3. ?섏씠吏쨌肄섑뀗痢졖룰린??怨꾩빟 / ## 4. ?ъ슜???먮쫫쨌?곹깭 / ## 5. 以묐났쨌?딄?쨌媛??寃利?- ?몄쬆쨌?섍꼍 ?④낵쨌?닿뎄 ?곗닔??異쒖쿂? ?뺤씤???놁씠 ?쒖떆?섏? ?딅뒗?? / ## 6. Mermaid / ## 7. ?먯젙

- Detail status: SOURCE-LINKED / MERGED
- No client-specific source section was discarded.

## Corrected A/B/C product reconciliation

- A products: PROD-025, PROD-026, PROD-055, PROD-057, PROD-093, PROD-094
- B products: PROD-025, PROD-026, PROD-055, PROD-057, PROD-093, PROD-094
- C products: PROD-025, PROD-026, PROD-055, PROD-057, PROD-093, PROD-094
- Final union: PROD-025, PROD-026, PROD-055, PROD-057, PROD-093, PROD-094
- Reconciliation status: PASS
