#include "stdio.h"
#include <stdlib.h>
#define nodeMAX 5

void weighted_union(int i, int j, int* parent);
int collapsing_find(int i, int* parent);

typedef struct
{
	int startNode;
	int endNode;
	int weight;
}edge;


void main() {
	int graph[nodeMAX][nodeMAX] = {
		{0,10,5,0,0,},
		{0,0,7,4,0},
		{0,0,0,3,2},
		{0,0,0,0,1},
		{0,0,0,0,0}
	};
	
	//[1] 그래프를 읽고 간선 연결 정보를 리스트로 만든다.
	edge eList[100];
	int edgeIdx = 0;
	for (int i = 0; i < nodeMAX; i++) {
		for (int j = 0; j < nodeMAX; j++) {
			//연결 정보 존재 -> 리스트에 추가
			if (graph[i][j] > 0) {
				eList[edgeIdx].startNode = i;
				eList[edgeIdx].endNode = j;
				eList[edgeIdx].weight = graph[i][j];
				edgeIdx++;
			}
		}
	}

	//[2] 간선의 가중치를 중심으로 오름차순을 진행
	int cntEdge = edgeIdx;
	for (int j = 0; j < cntEdge; j++) {
		for (int i = 0; i < cntEdge - 1; i++) {
			if (eList[i].weight > eList[i + 1].weight) {
				edge temp = eList[i];
				eList[i] = eList[i + 1];
				eList[i + 1] = temp;
			}
		}
	}

	//[3] 최소 간선 하나씩 끄집어내서 트리 생성

	//루트 노드 저장 배열
	
	int* parent;
	parent = (int*)malloc(sizeof(int) * cntEdge);
	for (int i = 0; i < cntEdge; i++) {
		parent[i] = -1;
	}

	//최종 MST트리 정보 저장
	edge MST[100];
	int cntTreeLine = 0;

	printf("\n---------------------------------------------\n");
	printf("\t# 크루스칼 알고리즘을 실행합니다.\n");
	printf("---------------------------------------------\n");
	for (int i = 0; i < cntEdge; i++) {
		edge minEdge = eList[i];

		//각 정점의 루트노드를 꺼낸다.
		int v1_set = collapsing_find(minEdge.startNode, parent);
		int v2_set = collapsing_find(minEdge.endNode, parent);

		//사이클 탐지
		if (v1_set == v2_set) {
			printf("[사이클 탐지] 간선 %c->%c는 루트가 %c로 일치\n",minEdge.startNode + 65, minEdge.endNode + 65, v2_set+65);
			printf("---------------------------------------------\n");
		}
		//사이클 X -> 트리에 추가
		else {
			printf("[이상 없음] [ %c - %c ] 간선 가중치 (%d) \n", minEdge.startNode+65, minEdge.endNode+65, minEdge.weight);
			printf("---------------------------------------------\n");
			MST[cntTreeLine].startNode = minEdge.startNode;
			MST[cntTreeLine].endNode = minEdge.endNode;
			cntTreeLine++;
			weighted_union(v1_set, v2_set, parent);
		}
	}
	printf("\n");
	printf("\t# 최종 parent배열 정보\n[parent] : ");
	for (int i = 0; i < cntEdge; i++) {
		printf("%d ", parent[i]);
	}
	printf("\n\n--------------------------------------------\n");

	printf("\n");
	printf("\t# MST 트리 정보\n");
	for (int i = 0; i < cntTreeLine; i++) {
		printf("\t    %c -> %c\n", MST[i].startNode+65, MST[i].endNode + 65);
	}
	printf("\n\n--------------------------------------------\n");
}

void weighted_union(int i, int j, int* parent) {
	int temp = parent[i] + parent[j];
	if (parent[i] >= parent[j]) {
		parent[i] = j;
		parent[j] = temp;
	}
	else {
		parent[j] = i;
		parent[i] = temp;
	}
}

int collapsing_find(int i, int* parent) {
	int root, trail, lead;

	//[1] 루트 노드 찾기 => root변수에 루트 노드를 담자
	for (root = i; parent[root] >= 0; root = parent[root]);

	//[2] 루트노드에 자식 노드 옮겨주기 => 루트까지 올라가면서 루트 노드에 붙여서 트리 높이 줄여주기
	for (trail = i; trail != root; trail = lead) {
		lead = parent[trail];
		parent[trail] = root;
	}
	return root;
}