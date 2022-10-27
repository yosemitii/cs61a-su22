(define (tail-replicate x n)
  ; BEGIN
  (define student-list '())
  (define (helper so_far times)
    ; (print so_far)
    (if (= times 0)
        so_far
        (helper (append so_far (list x)) (- times 1))
    )
    )
  (helper student-list n)
)