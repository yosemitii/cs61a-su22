(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
    (define (helper s i)
        (if (null? s)
            ()
            (append (list (list i (car s))) (helper (cdr s) (+ i 1)))
        )
    )
    (helper s 0)
  )
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to ORDERED? and return
;; the merged lists.
(define (merge ordered? list1 list2)
  ; BEGIN PROBLEM 16
    (cond
        ;((and (null? list1) (null? list2)) ())
        ((null? list1) list2);(list (car list2) (append (list (car list2)) (merge ordered? list1 (cdr list2)))))
        ((null? list2) list1);(list (car list1) (append (list (car list1)) (merge ordered? (cdr list1) list2))))
        (else
            (if (ordered? (car list1) (car list2))
                (append (list (car list1)) (merge ordered? (cdr list1) list2))
                (append (list (car list2)) (merge ordered? list1 (cdr list2)))
            )
        )
    )
)
  ; END PROBLEM 16

