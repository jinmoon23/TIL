// 컴포넌트 추출하기

import { getImageUrl } from './utils.js';

export default function Gallery() {
  return (
    <>
      <h1>Amazing scientists</h1>
      <Profile
        name="Alan L. Hart"
        imageId="szV5sdG"
        profession="Endocrinologist"
        awards={['Olive W. Garvey Distinguished Scientist Award']}
        discovery="First to use X-ray photography to study the human body"
        imageSize={70}
      />
      <Profile
        name="Alice Ball"
        imageId="YfeOqp2"
        profession="Chemist"
        awards={['Magazine Medal']}
        discovery="Ball developed the first successful treatment for leprosy"
        imageSize={70}
      />
    </>
  )
}

function Profile({ name, imageId, profession, awards, discovery, imageSize }) {
  return (
    <section className="profile">
      <h2>{name}</h2>
      <img
        className="avatar"
        src={getImageUrl(imageId)}
        alt={name}
        width={imageSize}
        height={imageSize}
      />
      <ul>
        <li>
          <b>Profession: </b>
          {profession}
        </li>
        <li>
          <b>Awards: {awards.length} </b>
          ({awards.join(', ')})
        </li>
        <li>
          <b>Discovered: </b>
          {discovery}
        </li>
      </ul>
    </section>
  );
}