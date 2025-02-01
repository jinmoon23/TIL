import { getImageUrl } from './utils.js';

function Avatar({ person, size }) {
  let dynamicSize = size < 90 ? 's' : 'b';
  return (
    <img
      className="avatar"
      src={getImageUrl(person, dynamicSize)}
      alt={person.name}
      width={dynamicSize}
      height={dynamicSize}
    />
  );
}

export default function Profile() {
  return (
    <Avatar
      size={40}
      person={{
        name: 'Gregorio Y. Zara',
        imageId: '7vQD0fP'
      }}
    />
  );
}
