# VC-46 지율-사이트구조맵 final design v1

Status: compare complete; merged final structure

Decision rules
- A is base.
- Merge unique B/C elements.
- REQ and Product IDs use union.

A/B/C comparison
A products: PROD-021, PROD-049, PROD-085, PROD-087
B products: PROD-021, PROD-049, PROD-085, PROD-087
C products: PROD-021, PROD-049, PROD-085, PROD-087
Common products: PROD-021, PROD-049, PROD-085, PROD-087
Merged products: 
REQ: REQ-046

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
PROD-021, PROD-049, PROD-085, PROD-087

Exceptions
- Keep unique elements as supplements.
- Unify duplicate functions.
- No product menu for no-product clients.
- Mark uncertain facts for verification.

Sources
Source folder: VC-46-지율-사이트구조맵-V3
A/B/C V3 MD MMD SVG

Gate: FINAL-MERGED / PASS

## Source-preserved client detail trace

- The following A/B/C V3 files are the authoritative client-specific detail sources.
- This final MD keeps the merged decision and points back to the complete source artifacts.

- A source: VC-46-지율-사이트구조맵-A안-V3-사이트맵.md
  Sections: ## 1. Client쨌REQ 異붿쟻 / ## 2. 援ъ“ ?꾨왂 / ## 3. ?섏씠吏쨌肄섑뀗痢졖룰린??怨꾩빟 / ## 4. ?ъ슜???먮쫫쨌?곹깭 / ## 5. 以묐났쨌?딄?쨌媛??寃利?- ?붿빟 移대뱶??諛섎났 ?뚯꽦 ??룆??以꾩씠怨??곸꽭 移대뱶濡??곌껐?쒕떎. / ## 6. Mermaid / ## 7. ?먯젙
- B source: VC-46-지율-사이트구조맵-B안-V3-사이트맵.md
  Sections: ## 1. Client쨌REQ 異붿쟻 / ## 2. 援ъ“ ?꾨왂 / ## 3. ?섏씠吏쨌肄섑뀗痢졖룰린??怨꾩빟 / ## 4. ?ъ슜???먮쫫쨌?곹깭 / ## 5. 以묐났쨌?딄?쨌媛??寃利?- ?泥??띿뒪?몃뒗 ?쒗뭹 ?섎?瑜???踰덈쭔 ?꾨떖?쒕떎. / ## 6. Mermaid / ## 7. ?먯젙
- C source: VC-46-지율-사이트구조맵-A안-V3-사이트맵.md
  Sections: ## 1. Client쨌REQ 異붿쟻 / ## 2. 援ъ“ ?꾨왂 / ## 3. ?섏씠吏쨌肄섑뀗痢졖룰린??怨꾩빟 / ## 4. ?ъ슜???먮쫫쨌?곹깭 / ## 5. 以묐났쨌?딄?쨌媛??寃利?- ?붿빟 移대뱶??諛섎났 ?뚯꽦 ??룆??以꾩씠怨??곸꽭 移대뱶濡??곌껐?쒕떎. / ## 6. Mermaid / ## 7. ?먯젙

- Detail status: SOURCE-LINKED / MERGED
- No client-specific source section was discarded.

## Corrected A/B/C product reconciliation

- A products: PROD-021, PROD-049, PROD-085, PROD-087
- B products: PROD-021, PROD-049, PROD-085, PROD-087
- C products: PROD-021, PROD-049, PROD-085, PROD-087
- Final union: PROD-021, PROD-049, PROD-085, PROD-087
- Reconciliation status: PASS
