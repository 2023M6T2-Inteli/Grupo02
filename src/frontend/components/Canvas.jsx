import React, { useRef, useEffect } from 'react';
import axios from 'axios';
import { AiOutlineMinus, AiFillDelete } from 'react-icons/ai';

const Canvas = ({ backgroundImageSrc, edge, modal_close, file, _name, _description, just_show = false }) => {

    async function SendSupabase() {

        const url = 'http://localhost:8000/images/send_supabase'; // URL da API de destino
        const formData = new FormData(); // Dados a serem enviados no corpo da requisição
        formData.append("file", file)
        console.log(formData)

        try {
            const image_url = await axios.post(url, formData);
            var graphData = {
                "image_address": image_url.data,
                "name": _name,
                "description": _description,
                "edges": edges.current
            }

            await axios.post("http://localhost:8000/graph/create", graphData);

            console.log('File uploaded successfully: ', image_url.data);
        } catch (error) {
            console.error('Error uploading file:', error);
        };

        modal_close(false)

    };


    const canvasRef = useRef(null);
    const nodes = useRef([]);
    const edges = useRef([]);
    const selection = useRef(null);
    const img = new Image();
    img.src = backgroundImageSrc;

    useEffect(() => {
        if (edge) {
            edge.forEach((edge_dic) => {
                const node_1 = {
                    x: edge_dic.from.x,
                    y: edge_dic.from.y,
                    radius: 10,
                    fillStyle: '#22CCCC',
                    strokeStyle: '#009999',
                    selectedFill: '#88AAAA',
                    selected: false,
                };

                nodes.current.push(node_1);
                const node_2 = {
                    x: edge_dic.target.x,
                    y: edge_dic.target.y,
                    radius: 10,
                    fillStyle: '#22CCCC',
                    strokeStyle: '#009999',
                    selectedFill: '#88AAAA',
                    selected: false,
                };

                nodes.current.push(node_2);

                edges.current.push({ from: node_1, to: node_2 });
            });
        }

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
            console.log("NOdes: ", nodes);
            console.log("Edges: ", edges);

            // Desenha todas as arestas, que são as linha entre dois nós que possuam conexão
            for (let i = 0; i < edges.current.length; i++) {
                const fromNode = edges.current[i].from;
                const toNode = edges.current[i].to;

                context.beginPath();
                context.strokeStyle = fromNode.strokeStyle;
                context.moveTo(fromNode.x, fromNode.y);
                context.lineTo(toNode.x, toNode.y);
                context.fillStyle = 'black';
                context.textAlign = 'center';
                var weight = (Math.sqrt((fromNode.x - toNode.x) ** 2 + (fromNode.y - toNode.y) ** 2)).toFixed(3);
                context.fillText(`W = ${weight}`,
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
                    let weight = (Math.sqrt((selection.current.x - target.x) ** 2 + (selection.current.y - target.y) ** 2)).toFixed(3)
                    edges.current.push({ from: selection.current, to: target, weight: weight });
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
        if (just_show == false) {
            canvas.addEventListener('mousedown', down);
            canvas.addEventListener('mousemove', move);
            canvas.addEventListener('mouseup', up);
            resize();
        }

        return () => {
            window.removeEventListener('resize', resize);
            canvas.removeEventListener('mousedown', down);
            canvas.removeEventListener('mousemove', move);
            canvas.removeEventListener('mouseup', up);
        };
    }, []);

    return (
        <div className='flex'>
            <div style={{ position: 'relative', width: '100%', height: '100%' }}>
                <canvas
                    ref={canvasRef}
                    className='border'
                    style={{
                        width: "100%",
                        height: "100%",
                        zIndex: 1,
                        backgroundImage: `url("${backgroundImageSrc}")`,
                        backgroundRepeat: 'no-repeat',
                        backgroundSize: 'contain',
                        // backgroundColor: 'rgba(218, 226, 234, 0.5)'
                    }} />
            </div>

            {!just_show && (
                <div className="w-3/12 flex flex-col items-center">
                    <div className="bg-azul cursor-pointer mb-8 flex flex-col rounded-2xl text-white items-center gap-y-1.5 p-8 H-max-15 W-max-20">
                        <div className='circulo'></div>
                        <span>Inserir nó</span>
                    </div>
                    <div className="bg-azul cursor-pointer mb-8 flex flex-col rounded-2xl text-white items-center gap-y-1.5 p-8 H-max-15 W-max-20">
                        <div className="text-4xl"><AiOutlineMinus /></div>
                        <span>Inserir aresta</span>
                    </div>
                    <div className="cursor-pointer bg-azul mb-8 flex flex-col rounded-2xl text-white items-center gap-y-1.5 p-8 H-max-15 W-max-20">
                        <div><AiFillDelete /></div>
                        <span>Deletar</span>
                    </div>
                    <button onClick={() => { SendSupabase() }} className='W-max-20 bg-azul rounded-2xl h-9 text-white'>save</button>
                </div>)}
        </div>
    );
};

export default Canvas;
