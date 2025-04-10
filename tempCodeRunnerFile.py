def fn(l ,r ):
    if ( l >= r ): return
    marks[l], marks[r] = marks[r], marks[l]
    fn(l+1, r-1)
fn(0, len(marks)-1)

print(marks)