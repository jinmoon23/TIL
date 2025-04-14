import { people } from './data.js';
import { getImageUrl } from './utils.js';

export default function List() {
  const chemistList = people.filter(person => person.profession === 'chemist');
  const others = people.filter(person => person.profession !== 'chemist');
  const chemistItems = chemistList.map(chemist =>
    <li key={chemist.id}>
      <img
        src={getImageUrl(chemist)}
        alt={chemist.name}
      />
      <p>
        <b>{chemist.name}:</b>
        {' ' + chemist.profession + ' '}
        known for {chemist.accomplishment}
      </p>
    </li>
  );
  const othersItems = others.map(other =>
    <li key={other.id}>
      <img
        src={getImageUrl(other)}
        alt={other.name}
      />
      <p>
        <b>{other.name}:</b>
        {' ' + other.profession + ' '}
        known for {other.accomplishment}
      </p>
    </li>
  )
  return (
    <article>
      <h1>Chemists</h1>
      <ul>{chemistItems}</ul>
      <h1>Others</h1>
      <ul>{othersItems}</ul>
    </article>
  );
}
