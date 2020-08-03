print(
    min(
        filter(
            lambda x: x % 2 == 1,
            list(
                map(
                    int,
                    input().split()
                )
            )
        )
    )
)
