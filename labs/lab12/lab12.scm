; Owner and Vehicle Abstraction
(define (make-owner name age)
  (cons name (cons age nil)))

(define (get-name owner) (car owner))

(define (get-age owner) (car (cdr owner)))

(define (make-vehicle model year previous-owners)
  (cons model (cons year previous-owners)))

(define (get-model vehicle)
    (car vehicle)
)

(define (get-year vehicle)
    (car (cdr vehicle))
)

(define (get-owners vehicle)
    (define (helper lst)
        (if (eq? (cdr lst) nil)
            (list (car lst))
            (append (list (car lst)) (helper (cdr lst)))
        )
    )
    ;(car (cdr (cdr vehicle)))
    (helper (cdr (cdr vehicle)))
)

(define (older-vehicle vehicle1 vehicle2)
    (if (< (get-year vehicle1) (get-year vehicle2))
        (get-model vehicle1)
        (get-model vehicle2)
    )
)

(define (new-owner vehicle owner)
    ;(define new-owners (append (get-owners vehicle) (list owner)))
    ;(append (get-owners vehicle) (list owner))
    (make-vehicle (get-model vehicle) (get-year vehicle) (append (list owner) (get-owners vehicle)))
)

(define (owners-names vehicle)
    (define (helper lst)
        (if (null? lst)
            ()
            (append (list (car (car lst))) (helper(cdr lst)))
        )
    )
    (helper (get-owners vehicle))
)

(define (split-at lst n)
    (define (helper lst n)
            (if (> n 0)
                (append (list (car lst)) (helper (cdr lst) (- n 1)))
                nil
            )
    )
    (define (helper2 lst n)
        (if (> n 0)
            (helper2 (cdr lst) (- n 1))
            lst
        )
    )
    (if (<= (length lst) n)
        (cons lst nil)
        (append (list (helper lst n )) (helper2 lst n))
    )
)

; Tree Abstraction
; Constructs tree given label and list of branches
(define (tree label branches)
  (cons label branches))

; Returns the label of the tree
(define (label t) (car t))

; Returns the list of branches of the given tree
(define (branches t) (cdr t))

; Returns #t if t is a leaf, #f otherwise
(define (is-leaf t) (null? (branches t)))

(define (filter-odd t)
    (if (is-leaf t)
        (if (odd? (label t))
            (tree (label t) nil)
            (tree nil nil)
        )
        (if (odd? (label t))
            (tree (label t) (map filter-odd (branches t)))
            (tree nil (map filter-odd (branches t)))
        )
    )

)
