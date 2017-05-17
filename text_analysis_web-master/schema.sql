drop table if exists entries;
create table entries(
    id              integer primary key autoincrement,
    --username        text    default 'Default User',
    topic0          text    not null,
    topic1          text    not null,
    topic2          text    not null,
    title           text    not null,
    sentences       integer not null,
    words           integer not null,
    syllables       integer not null,
    characters      integer not null,
    polysyllables   integer not null,
    re              integer not null,
    gl              integer not null,
    ari             integer not null,
    smog            integer not null
);
