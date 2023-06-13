import Pop_up_edit from "./Pop_up_edit";

export default function Registration({ name, description, image_address, nodes, edges }) {
    return (
        <div className="flex pl-2 py-4 pr-6 bg-componentes w-5/6 h-12 rounded-lg my-4 flex justify-between">
            <span style={{ cursor: 'pointer' }} className="text-primary">
                {name}
            </span>
            <Pop_up_edit name={name} description={description} image_address={image_address} nodes={nodes} edges={edges} />
        </div>
    );
}
