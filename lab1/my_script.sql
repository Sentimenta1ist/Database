--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4
-- Dumped by pg_dump version 12.4

-- Started on 2020-09-21 07:48:52

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 206 (class 1259 OID 16420)
-- Name: friends; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.friends (
    status character varying NOT NULL,
    id integer NOT NULL,
    id_user character varying NOT NULL
);


ALTER TABLE public.friends OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 16418)
-- Name: friends_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.friends ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.friends_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 210 (class 1259 OID 16450)
-- Name: groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.groups (
    id integer NOT NULL,
    name character varying NOT NULL,
    description character varying,
    owner character varying NOT NULL,
    date date NOT NULL
);


ALTER TABLE public.groups OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 16448)
-- Name: group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.groups ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 208 (class 1259 OID 16435)
-- Name: posts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.posts (
    description character varying NOT NULL,
    date character varying NOT NULL,
    title character varying NOT NULL,
    likes integer NOT NULL,
    id integer NOT NULL,
    id_walls integer NOT NULL
);


ALTER TABLE public.posts OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 16433)
-- Name: posts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.posts ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.posts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 202 (class 1259 OID 16395)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    login character varying NOT NULL,
    name character varying NOT NULL,
    password character varying NOT NULL,
    phone character varying NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 16460)
-- Name: users_groups_rel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_groups_rel (
    user_fk character varying NOT NULL,
    groups_fk integer NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.users_groups_rel OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 16458)
-- Name: users_groups_rel_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.users_groups_rel ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.users_groups_rel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 204 (class 1259 OID 16405)
-- Name: walls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.walls (
    id integer NOT NULL,
    id_user character varying NOT NULL,
    info character varying
);


ALTER TABLE public.walls OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 16403)
-- Name: wall_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.walls ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.wall_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 2726 (class 2606 OID 16427)
-- Name: friends friends_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.friends
    ADD CONSTRAINT friends_pkey PRIMARY KEY (id);


--
-- TOC entry 2730 (class 2606 OID 16457)
-- Name: groups group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.groups
    ADD CONSTRAINT group_pkey PRIMARY KEY (id);


--
-- TOC entry 2728 (class 2606 OID 16442)
-- Name: posts posts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (id);


--
-- TOC entry 2722 (class 2606 OID 16402)
-- Name: users user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT user_pkey PRIMARY KEY (phone);


--
-- TOC entry 2732 (class 2606 OID 16477)
-- Name: users_groups_rel users_groups_rel_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_groups_rel
    ADD CONSTRAINT users_groups_rel_pkey PRIMARY KEY (id);


--
-- TOC entry 2724 (class 2606 OID 16412)
-- Name: walls wall_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.walls
    ADD CONSTRAINT wall_pkey PRIMARY KEY (id);


--
-- TOC entry 2737 (class 2606 OID 16471)
-- Name: users_groups_rel id_groups; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_groups_rel
    ADD CONSTRAINT id_groups FOREIGN KEY (groups_fk) REFERENCES public.groups(id);


--
-- TOC entry 2734 (class 2606 OID 16428)
-- Name: friends id_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.friends
    ADD CONSTRAINT id_user FOREIGN KEY (id_user) REFERENCES public.users(phone);


--
-- TOC entry 2733 (class 2606 OID 16413)
-- Name: walls id_user_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.walls
    ADD CONSTRAINT id_user_fk FOREIGN KEY (id_user) REFERENCES public.users(phone);


--
-- TOC entry 2736 (class 2606 OID 16466)
-- Name: users_groups_rel id_users; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_groups_rel
    ADD CONSTRAINT id_users FOREIGN KEY (user_fk) REFERENCES public.users(phone);


--
-- TOC entry 2735 (class 2606 OID 16443)
-- Name: posts id_walls; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT id_walls FOREIGN KEY (id_walls) REFERENCES public.walls(id);


-- Completed on 2020-09-21 07:48:52

--
-- PostgreSQL database dump complete
--

