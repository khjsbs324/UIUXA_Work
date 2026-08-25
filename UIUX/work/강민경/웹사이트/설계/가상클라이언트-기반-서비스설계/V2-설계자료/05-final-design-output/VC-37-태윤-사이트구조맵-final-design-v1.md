# VC-37 태윤-사이트구조맵 final design v1

Status: compare complete; merged final structure

Decision rules
- A is base.
- Merge unique B/C elements.
- REQ and Product IDs use union.

A/B/C comparison
A products: PROD-010, PROD-018, PROD-041, PROD-073, PROD-084
B products: PROD-010, PROD-018, PROD-041, PROD-073, PROD-084
C products: PROD-010, PROD-018, PROD-041, PROD-073, PROD-084
Common products: PROD-010, PROD-018, PROD-041, PROD-073, PROD-084
Merged products: 
REQ: REQ-037

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
PROD-010, PROD-018, PROD-041, PROD-073, PROD-084

Exceptions
- Keep unique elements as supplements.
- Unify duplicate functions.
- No product menu for no-product clients.
- Mark uncertain facts for verification.

Sources
Source folder: VC-37-태윤-사이트구조맵-V3
A/B/C V3 MD MMD SVG

Gate: FINAL-MERGED / PASS

## Source-preserved client detail trace

- The following A/B/C V3 files are the authoritative client-specific detail sources.
- This final MD keeps the merged decision and points back to the complete source artifacts.

- A source: VC-37-태윤-사이트구조맵-A안-V3-사이트맵.md
  Sections: ## 1. Client쨌REQ 異붿쟻 / ## 2. 援ъ“ ?꾨왂 / ## 3. ?섏씠吏쨌肄섑뀗痢졖룰린??怨꾩빟 / ## 4. ?ъ슜???먮쫫쨌?곹깭 / ## 5. 以묐났쨌?딄?쨌媛??寃利?- ?쒗쁽쨌湲곕뒫 ?쇰꺼? 肄섑뀗痢좎? ?쒗뭹 湲곕뒫??援щ텇?섎뒗 ?쒖떇?대떎. / ## 6. Mermaid / ## 7. ?먯젙
- B source: VC-37-태윤-사이트구조맵-B안-V3-사이트맵.md
  Sections: ## 1. Client쨌REQ 異붿쟻 / ## 2. 援ъ“ ?꾨왂 / ## 3. ?섏씠吏쨌肄섑뀗痢졖룰린??怨꾩빟 / ## 4. ?ъ슜???먮쫫쨌?곹깭 / ## 5. 以묐났쨌?딄?쨌媛??寃利?- 愿???쒗뭹? ?먯깋 ??곸씠吏 媛?대뱶???꾩닔 寃곕줎???꾨땲?? / ## 6. Mermaid / ## 7. ?먯젙
- C source: VC-37-태윤-사이트구조맵-A안-V3-사이트맵.md
  Sections: ## 1. Client쨌REQ 異붿쟻 / ## 2. 援ъ“ ?꾨왂 / ## 3. ?섏씠吏쨌肄섑뀗痢졖룰린??怨꾩빟 / ## 4. ?ъ슜???먮쫫쨌?곹깭 / ## 5. 以묐났쨌?딄?쨌媛??寃利?- ?쒗쁽쨌湲곕뒫 ?쇰꺼? 肄섑뀗痢좎? ?쒗뭹 湲곕뒫??援щ텇?섎뒗 ?쒖떇?대떎. / ## 6. Mermaid / ## 7. ?먯젙

- Detail status: SOURCE-LINKED / MERGED
- No client-specific source section was discarded.

## Corrected A/B/C product reconciliation

- A products: PROD-010, PROD-018, PROD-041, PROD-073, PROD-084
- B products: PROD-010, PROD-018, PROD-041, PROD-073, PROD-084
- C products: PROD-010, PROD-018, PROD-041, PROD-073, PROD-084
- Final union: PROD-010, PROD-018, PROD-041, PROD-073, PROD-084
- Reconciliation status: PASS
