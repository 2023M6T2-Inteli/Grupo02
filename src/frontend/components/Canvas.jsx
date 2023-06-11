import React, { useRef, useEffect } from 'react';

const Canvas = ({ backgroundImageSrc, node, edge }) => {
    const canvasRef = useRef(null);
    const nodes = useRef([]);
    const edges = useRef([]);
    const selection = useRef(null);
    const img = new Image();
    img.src = backgroundImageSrc;


                   
    useEffect(() => {
        node.forEach((node_dic) => {
            const node_map = {
                x: node_dic.x,
                y: node_dic.y,
                radius: 10,
                fillStyle: '#22CCCC',
                strokeStyle: '#009999',
                selectedFill: '#88AAAA',
                selected: false,
            };

            nodes.current.push(node_map);
        });
        edge.forEach((edge_dic) => {
            
            edges.current.push({ from: {x:edge_dic.from_x,y:edge_dic.from_y}, to: {x:edge_dic.target_x,y:edge_dic.target_y} });
        });

        console.log(edges.current)
        const canvas = canvasRef.current;
        const context = canvas.getContext('2d');
        context.font = '30px Arial';

        const resize = () => {
            canvas.width = canvas.offsetWidth;
            canvas.height = canvas.offsetHeight;
            draw();
        };

        // const drawImage = () => {
        //     const image = new Image();
        //     image.src = backgroundImageSrc;
        //     image.onload = () => {
        //         context.drawImage(image, 0, 0, canvas.width, canvas.height);
        //     };
        // };

        const getCanvasOffset = (e) => {
            const rect = canvas.getBoundingClientRect();
            const offsetX = e.clientX - rect.left;
            const offsetY = e.clientY - rect.top;
            return { offsetX, offsetY };
        };


        const draw = () => {
            context.clearRect(0, 0, canvas.width, canvas.height);

            // Desenhar a imagem de plano de fundo
            // drawImage();
            console.log('nodes:', nodes)
            console.log('edges:', edges)

            // Desenha todas as arestas, que são as linha entre dois nós que possuam conexão
            for (let i = 0; i < edges.current.length; i++) {
                const fromNode = edges.current[i].from;
                const toNode = edges.current[i].to;

                context.beginPath();
                context.strokeStyle = fromNode.strokeStyle;
                context.moveTo(fromNode.x, fromNode.y);
                context.lineTo(toNode.x, toNode.y);
                context.fillStyle = 'red';
                context.textAlign = 'center';
                context.fillText(`W = ${(Math.sqrt((fromNode.x - toNode.x) ** 2 + (fromNode.y - toNode.y) ** 2)).toFixed(3)}`,
                    toNode.x + ((toNode.x - fromNode.x) * -1) / 2,
                    toNode.y + ((toNode.y - fromNode.y) * -1) / 2)
                context.stroke();
            }

            // Desenha todos os nós, que são círculos azuis com texto 
            for (let i = 0; i < nodes.current.length; i++) {
                const node = nodes.current[i];

                context.beginPath();
                context.fillStyle = node.selected ? node.selectedFill : node.fillStyle;
                context.arc(node.x, node.y, node.radius, 0, Math.PI * 2, true);
                context.strokeStyle = node.strokeStyle;
                context.fill();
                context.fillStyle = 'black';
                context.textAlign = 'center';
                context.fillText(`${Math.round(node.x)} ; ${Math.round(node.y)}`,
                    node.x,
                    node.y);
                context.stroke();
            }

        };

        const within = (x, y) => {
            return nodes.current.find((n) => {
                return (
                    x > n.x - n.radius &&
                    y > n.y - n.radius &&
                    x < n.x + n.radius &&
                    y < n.y + n.radius
                );
            });
        };

        const down = (e) => {
            const { offsetX, offsetY } = getCanvasOffset(e);
            const target = within(offsetX, offsetY);

            if (selection.current && selection.current.selected) {
                selection.current.selected = false;
            }

            if (target) {
                if (selection.current && selection.current !== target) {
                    edges.current.push({ from: selection.current, to: target });
                }

                selection.current = target;
                selection.current.selected = true;
                draw();
            }
        };

        const move = (e) => {
            if (selection.current && e.buttons) {
                const { offsetX, offsetY } = getCanvasOffset(e);
                selection.current.x = offsetX;
                selection.current.y = offsetY;
                draw();
            }
        };

        const up = (e) => {
            if (!selection.current) {
                const { offsetX, offsetY } = getCanvasOffset(e);
                const node = {
                    x: offsetX,
                    y: offsetY,
                    radius: 10,
                    fillStyle: '#22CCCC',
                    strokeStyle: '#009999',
                    selectedFill: '#88AAAA',
                    selected: false,
                };

                nodes.current.push(node);
                draw();
            }

            if (selection.current && !selection.current.selected) {
                selection.current = null;
            }

            draw();
        };

        window.addEventListener('resize', resize);
        canvas.addEventListener('mousedown', down);
        canvas.addEventListener('mousemove', move);
        canvas.addEventListener('mouseup', up);

        resize();

        return () => {
            window.removeEventListener('resize', resize);
            canvas.removeEventListener('mousedown', down);
            canvas.removeEventListener('mousemove', move);
            canvas.removeEventListener('mouseup', up);
        };
    }, []);

    return (
        <div style={{ position: 'relative', width: '100%', height: '100%' }}>
            <canvas
                ref={canvasRef}
                className='border'
                style={{
                    width: "100%",
                    height:"100%",
                    zIndex: 1,
                    backgroundImage: `url("${backgroundImageSrc}")`,
                    backgroundRepeat: 'no-repeat',
                    backgroundSize: 'contain',
                    // backgroundColor: 'rgba(218, 226, 234, 0.5)'
                }} />
        </div>
    );
};

export default Canvas;
