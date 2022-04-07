begin
    execute immediate 'drop table geoclientlogmine';
exception
    when others then
      if sqlcode = -942 then
        null; 
      else
         raise;
      end if;
end;


create table geoclientlogmine (
    id          number generated always as identity
   ,inputfile   varchar2(64)
   ,ip          varchar2(16)
   ,gcdate      varchar2(32)
   ,getreq      varchar2(4000)
   ,httpcode    varchar2(4)
);

create bitmap index 
    geoclientlogmineinputfile 
on 
    geoclientlogmine(inputfile);

create bitmap index 
    geoclientlogmineip
on 
    geoclientlogmine(ip);

create index 
    geoclientlogminegetreq
on
    geoclientlogmine(getreq);