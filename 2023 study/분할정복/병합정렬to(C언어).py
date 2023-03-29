//크기 비교를 하고 합치자
	//그냥 바로 좌우 합치려고 하니 인덱스 조정이..
	//
	int leftIdx = 0;
	int rightIdx = 0;
	int curIdx = 0;
	for(int i = 0; i < tempLen; i++){
		//좌우 비교하자
		if(leftPart[leftIdx] < rightPart[rightIdx]){
			tempAry[i] = rightIdx[i];
			leftIdx++;
		}
		else if{
			tempAry[i] = leftPart[i];
			rightIdx++;
		}
	}


#include <stdio.h>
#include <stdlib.h>

int* arrSlicing(int* ary, int start, int end) {
	printf("시작 : %d | 끝 : %d \n", start, end);
	int maxIdx = (end - start);
	int* sliceArr = (int*)malloc(sizeof(int) * (maxIdx+1));

	// 슬라이싱 결과 배열에 값 대입
	for (int i = 0; i <= maxIdx; i++) {
		sliceArr[i] = ary[start + i];
	}

	for (int i = 0; i <= maxIdx; i++) {
		printf("슬라이싱 결과[%d] : %d (길이 : %d)\n", i,sliceArr[i], sizeof(sliceArr));
	}
	printf("\n");
	return sliceArr;
}

int* mergeSort(int ary[])
{
	int aryLen = sizeof(ary);
	printf("--------------------\n");
	printf("길이 : %d\n", aryLen);
	if (aryLen < 2) {
		return ary;
	}

	//왼쪽, 오른쪽으로 계속 나눠주자
	int* leftPart = arrSlicing(ary, 0, (aryLen / 2) - 1); // 0~2
	printf("\n슬라이싱 확인[%d] ", sizeof(leftPart));
	for (int i = 0; i < sizeof(leftPart) / 2; i++) {
		printf("%d ", leftPart[i]);
	}
	printf("\n");
	leftPart = mergeSort(leftPart);
	int* rightPart = arrSlicing(ary, (aryLen / 2) - 1, aryLen - 1);//2~4
	rightPart = mergeSort(rightPart);

	//<------------합병 시작--------------->
	printf("합병 좌측: ");
	for (int idx = 0; idx < (sizeof(leftPart) / sizeof(int)); idx++)
	{
		printf("%d : %d | ", idx, leftPart[idx]);
	}
	printf("\n합병 우측 : ");
	for (int idx = 0; idx < sizeof(rightPart) / sizeof(int); idx++)
	{
		printf("%d : %d | ", idx, rightPart[idx]);
	}
	printf("\n");

	//담아낼 임시 배열 및 최종 반환 배열
	int tempLen = sizeof(leftPart) / sizeof(int) + sizeof(rightPart) / sizeof(int);
	int* tempAry = (int*)malloc(sizeof(int) * tempLen);

	//크기 비교를 하고 합치자
	int leftIdx = 0;
	int rightIdx = 0;
	int curIdx = 0;
	//인덱스 넘지 않는 선에서 일단 합쳐본다.
	while (leftIdx < (sizeof(leftPart) / sizeof(int)) && rightIdx < (sizeof(rightPart) / sizeof(int)))
	{
		if (leftPart[leftIdx] < rightPart[rightIdx]) {
			tempAry[curIdx] = rightPart[rightIdx];
			rightIdx++;
		}
		else {
			tempAry[curIdx] = leftPart[leftIdx];
			leftIdx++;
		}
		curIdx++;
	}
	//합치고 남는 거 합치자
	if (leftIdx != sizeof(leftPart) / sizeof(int)) {
		for (int LIdx = leftIdx; LIdx < sizeof(leftPart) / sizeof(int); LIdx++) {
			tempAry[curIdx] = leftPart[LIdx];
			curIdx++;
		}
	}
	if (rightIdx != sizeof(rightPart) / sizeof(int)) {
		for (int RIdx = rightIdx; RIdx < sizeof(rightPart) / sizeof(int); RIdx++) {
			tempAry[curIdx] = rightPart[RIdx];
			curIdx++;
		}
	}
	return tempAry;
}

void main()
{
	int ary[] = {4,3,2,1};
	printf("길이 : %d\n", sizeof(ary));
	int* lastAry = mergeSort(ary);
	printf("최종 배열 : ");
	for (int i = 0; i < 4; i++) {
		printf("%d ", lastAry[i]);
	}
}