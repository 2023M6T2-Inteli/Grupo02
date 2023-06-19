import Pop_up_edit from "./Pop_up_edit";

<<<<<<< HEAD
export default function Registration({ name, description, image_address, id }) {
    return (
=======
export default function Registration({id, name, description, image}) {
    return(
>>>>>>> 8bafb163b2a34169447e2f4aeac95d0a6d8cf17f
        <div className="flex pl-2 py-4 pr-6 bg-componentes w-5/6 h-12 rounded-lg my-4 flex justify-between">
            <span style={{ cursor: 'pointer' }} className="text-primary">
                {name}
            </span>
<<<<<<< HEAD
            <Pop_up_edit name={name} description={description} image_address={image_address} id={id} />
=======
            <Pop_up_edit id={id} name={name} description={description} image={image} />
>>>>>>> 8bafb163b2a34169447e2f4aeac95d0a6d8cf17f
        </div>
    );
}
