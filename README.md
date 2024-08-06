# Teknofest_TDI
Teknofest 2024 NLP (Türkçe Doğal Dil İşleme) Yarışması Github Projesi


<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Neural Network</title>
    <style>
        body {
            background-color: rgb(209, 209, 209);
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            overflow-x: auto;
        }

        .network {
            display: flex;
            align-items: center;
            position: relative;
        }

        .layer {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 10px;
        }

        .node {
            background-color: rgb(44, 44, 44);
            border-radius: 15px;
            margin: 5px 0;
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            font-size: 12px;
            font-weight: bold;
            padding: 5px;
            box-sizing: border-box;
            min-width: 80px;
            min-height: 40px;
            transition: all 0.3s ease;
            text-align: center;
        }

        .node:hover {
            background-color: rgb(28, 40, 51);
        }

        .node.highlight {
            background-color: rgb(200, 16, 46) !important;
        }

        .node.highlight-text {
            background-color: blue !important;
        }

        .node::after {
            content: '';
            position: absolute;
            width: 100%;
            height: 100%;
            border: 1px solid transparent;
            border-radius: 15px;
        }

        /* .layer:hover .node::after {
            border-color: red;
        } */

        .output-layer {
            display: flex;
            flex-wrap: wrap;
            flex-direction: row;
            align-items: flex-start;
            width: auto;
            height: auto;
            position: relative;
            margin-left: 20px;
            margin-top: 10px;
        }

        .output-layer .node {
            margin: 5px;
            width: 80px;
            height: 40px;
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="network" id="network">
        <!-- Layers will be generated dynamically -->
    </div>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const layerNodeCounts = [1, 2, 4, 1];
            const networkElement = document.getElementById('network');
            const nodeValues = [
                ["Data Temizleme"],
                ["Spacy StopWords", "Kendi Stopwords"],
                ["ELECTRA Base mC4 (cased)", "BERTurk (cased, 32k)", "ConvBERTurk mC4 (uncased)", "gpt-2"],
                ["PyTorch"]
            ];

            const combinationNames = [
                "Combination 1",
                "Combination 2",
                "Combination 3",
                "Combination 4",
                "Combination 5",
                "Combination 6",
                "Combination 7",
                "Combination 8",
                "Combination 9",
                "Combination 10",
                "Combination 11",
                "Combination 12",
                "Combination 13",
                "Combination 14",
                "Combination 15",
                "Combination 16",
                "Combination 17",
                "Combination 18",
                "Combination 19",
                "Combination 20",
                "Combination 21",
                "Combination 22",
                "Combination 23",
                "Combination 24", 
                "Combination 1",
                "Combination 2",
                "Combination 3",
                "Combination 4",
                "Combination 5",
                "Combination 6",
                "Combination 7",
                "Combination 8",
                "Combination 9",
                "Combination 10",
                "Combination 11",
                "Combination 12",
                "Combination 13",
                "Combination 14",
                "Combination 15",
                "Combination 16",
                "Combination 17",
                "Combination 18",
                "Combination 19",
                "Combination 20",
                "Combination 21",
                "Combination 22",
                "Combination 23",
                "Combination 24", 
                "Combination 1",
                "Combination 2",
                "Combination 3",
                "Combination 4",
                "Combination 5",
                "Combination 6",
                "Combination 7",
                "Combination 8",
                "Combination 9",
                "Combination 10",
                "Combination 11",
                "Combination 12",
                "Combination 13",
                "Combination 14",
                "Combination 15",
                "Combination 16",
                "Combination 17",
                "Combination 18",
                "Combination 19",
                "Combination 20",
                "Combination 21",
                "Combination 22",
                "Combination 23",
                "Combination 24", 
                "Combination 1",
                "Combination 2",
                "Combination 3",
                "Combination 4",
                "Combination 5",
                "Combination 6",
                "Combination 7",
                "Combination 8",
                "Combination 9",
                "Combination 10",
                "Combination 11",
                "Combination 12",
                "Combination 13",
                "Combination 14",
                "Combination 15",
                "Combination 16",
                "Combination 17",
                "Combination 18",
                "Combination 19",
                "Combination 20",
                "Combination 21",
                "Combination 22",
                "Combination 23",
                "Combination 24"
            ];

            function createNode(layerIndex, nodeIndex, value) {
                const node = document.createElement('div');
                node.classList.add('node');
                node.dataset.layer = layerIndex;
                node.dataset.node = nodeIndex;
                node.innerText = value;
                node.dataset.value = value;
                return node;
            }

            function createLayer(layerIndex, nodeCount, values) {
                const layer = document.createElement('div');
                layer.classList.add('layer');
                layer.dataset.layer = layerIndex;
                for (let i = 0; i < nodeCount; i++) {
                    layer.appendChild(createNode(layerIndex, i, values[i]));
                }
                return layer;
            }

            for (let i = 0; i < layerNodeCounts.length; i++) {
                networkElement.appendChild(createLayer(i + 1, layerNodeCounts[i], nodeValues[i]));
            }

            const previousLayers = layerNodeCounts.map((count, index) => {
                return Array.from({ length: count }, (_, i) => createNode(index + 1, i, nodeValues[index][i]));
            });

            function generateCombinations(layers) {
                if (layers.length === 0) return [[]];
                const firstLayer = layers[0];
                const restCombinations = generateCombinations(layers.slice(1));
                const combinations = [];
                for (const node of firstLayer) {
                    for (const combination of restCombinations) {
                        combinations.push([node, ...combination]);
                    }
                }
                return combinations;
            }

            const combinations = generateCombinations(previousLayers);

            function createOutputNode(combination, index, name) {
                const node = document.createElement('div');
                node.classList.add('node');
                node.dataset.combination = combination.map(node => `${node.dataset.layer}-${node.dataset.node}`).join(',');
                node.innerText = name;
                return node;
            }

            const outputLayer = document.createElement('div');
            outputLayer.classList.add('layer', 'output-layer');
            outputLayer.dataset.layer = layerNodeCounts.length + 1;
            combinations.forEach((combination, index) => {
                outputLayer.appendChild(createOutputNode(combination, index, combinationNames[index] || `Combination ${index + 1}`));
            });
            networkElement.appendChild(outputLayer);

            function updateNodeSizes() {
                let maxValue = 0;
                document.querySelectorAll('.node').forEach(node => {
                    const value = parseInt(node.dataset.value);
                    if (value > maxValue) {
                        maxValue = value;
                    }
                });

                document.querySelectorAll('.node').forEach(node => {
                    const value = parseInt(node.dataset.value);
                    const size = Math.max((value / maxValue) * 80, 40);
                    node.style.width = `${size + 20}px`;
                    node.style.height = `${size}px`;
                });
            }

            updateNodeSizes();

            const layers = previousLayers.map((_, index) => 
                document.querySelectorAll(`.layer[data-layer="${index + 1}"] .node`)
            );

            const outputNodes = outputLayer.querySelectorAll('.node');
            outputNodes.forEach(outputNode => {
                outputNode.addEventListener('mouseenter', () => {
                    const combination = outputNode.dataset.combination.split(',');
                    combination.forEach(nodeId => {
                        const [layer, node] = nodeId.split('-');
                        document.querySelector(`.layer[data-layer="${layer}"] .node[data-node="${node}"]`).classList.add('highlight');
                    });
                    outputNode.classList.add('highlight');
                });

                outputNode.addEventListener('mouseleave', () => {
                    const combination = outputNode.dataset.combination.split(',');
                    combination.forEach(nodeId => {
                        const [layer, node] = nodeId.split('-');
                        document.querySelector(`.layer[data-layer="${layer}"] .node[data-node="${node}"]`).classList.remove('highlight');
                    });
                    outputNode.classList.remove('highlight');
                });
            });

            document.querySelectorAll(`.layer:not([data-layer="${layerNodeCounts.length + 1}"])`).forEach(layer => {
                layer.addEventListener('mouseenter', () => {
                    layer.querySelectorAll('.node').forEach(node => {
                        node.classList.remove('highlight');
                    });
                });

                layer.addEventListener('mouseleave', () => {
                    layer.querySelectorAll('.node').forEach(node => {
                        node.classList.remove('highlight');
                    });
                });
            });
        });
    </script>
</body>
</html>
