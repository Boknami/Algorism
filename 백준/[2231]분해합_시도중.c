#include<stdio.h>

void main()
{
	int N = 0;
	scanf_s("%d", &N);

	//N 을 나타내기 위한 숫자
	//=> 생성자 M + 각 자리 숫자 합 => N

	//245의 분해합 => 256의 생성자
	//각 자리의 숫자를 뽑아낼 수 있어야겠는걸?

	//각 자리 전부 뽑아내고 특정 숫자부터 더해?

	//216으로 해보자
	//어떤 숫자는 X + 각 자리 숫자해서 216이 나온다는거임

	int X = 0;
	X = N - 27;

	int check = 0;
	check = N - 27;

	int Sum_digit = 0;

	int dig = 0;
	int count = 0;

	//자릿수 체크
	while ( N >= 0)
	{
		if (N > 10)
		{
			N = N / 10;
			count++;
		}
		else
			break;
	}
	
	printf("%d", count);
	while (X <= N)
	{
		
		X = X + Sum_digit;
	}
}