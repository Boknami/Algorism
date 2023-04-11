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
	
	//[1] �׷����� �а� ���� ���� ������ ����Ʈ�� �����.
	edge eList[100];
	int edgeIdx = 0;
	for (int i = 0; i < nodeMAX; i++) {
		for (int j = 0; j < nodeMAX; j++) {
			//���� ���� ���� -> ����Ʈ�� �߰�
			if (graph[i][j] > 0) {
				eList[edgeIdx].startNode = i;
				eList[edgeIdx].endNode = j;
				eList[edgeIdx].weight = graph[i][j];
				edgeIdx++;
			}
		}
	}

	//[2] ������ ����ġ�� �߽����� ���������� ����
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

	//[3] �ּ� ���� �ϳ��� ������� Ʈ�� ����

	//��Ʈ ��� ���� �迭
	
	int* parent;
	parent = (int*)malloc(sizeof(int) * cntEdge);
	for (int i = 0; i < cntEdge; i++) {
		parent[i] = -1;
	}

	//���� MSTƮ�� ���� ����
	edge MST[100];
	int cntTreeLine = 0;

	printf("\n---------------------------------------------\n");
	printf("\t# ũ�罺Į �˰����� �����մϴ�.\n");
	printf("---------------------------------------------\n");
	for (int i = 0; i < cntEdge; i++) {
		edge minEdge = eList[i];

		//�� ������ ��Ʈ��带 ������.
		int v1_set = collapsing_find(minEdge.startNode, parent);
		int v2_set = collapsing_find(minEdge.endNode, parent);

		//����Ŭ Ž��
		if (v1_set == v2_set) {
			printf("[����Ŭ Ž��] ���� %c->%c�� ��Ʈ�� %c�� ��ġ\n",minEdge.startNode + 65, minEdge.endNode + 65, v2_set+65);
			printf("---------------------------------------------\n");
		}
		//����Ŭ X -> Ʈ���� �߰�
		else {
			printf("[�̻� ����] [ %c - %c ] ���� ����ġ (%d) \n", minEdge.startNode+65, minEdge.endNode+65, minEdge.weight);
			printf("---------------------------------------------\n");
			MST[cntTreeLine].startNode = minEdge.startNode;
			MST[cntTreeLine].endNode = minEdge.endNode;
			cntTreeLine++;
			weighted_union(v1_set, v2_set, parent);
		}
	}
	printf("\n");
	printf("\t# ���� parent�迭 ����\n[parent] : ");
	for (int i = 0; i < cntEdge; i++) {
		printf("%d ", parent[i]);
	}
	printf("\n\n--------------------------------------------\n");

	printf("\n");
	printf("\t# MST Ʈ�� ����\n");
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

	//[1] ��Ʈ ��� ã�� => root������ ��Ʈ ��带 ����
	for (root = i; parent[root] >= 0; root = parent[root]);

	//[2] ��Ʈ��忡 �ڽ� ��� �Ű��ֱ� => ��Ʈ���� �ö󰡸鼭 ��Ʈ ��忡 �ٿ��� Ʈ�� ���� �ٿ��ֱ�
	for (trail = i; trail != root; trail = lead) {
		lead = parent[trail];
		parent[trail] = root;
	}
	return root;
}