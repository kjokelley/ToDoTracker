--
-- PostgreSQL database dump
--

\restrict fH0eRquJLW1F6djfwWs3FudhyT0csnxwOVrOQyn73tYO8rdNM8blzxo2wCS99TB

-- Dumped from database version 18.4 (Homebrew)
-- Dumped by pg_dump version 18.4 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- Name: tasks; Type: TABLE; Schema: public; Owner: kyle
--

CREATE TABLE public.tasks (
    id integer NOT NULL,
    name text NOT NULL,
    type text NOT NULL,
    priority integer NOT NULL,
    completed boolean DEFAULT false NOT NULL,
    created_date date DEFAULT CURRENT_DATE,
    completed_date date,
    recurring boolean DEFAULT false
);


ALTER TABLE public.tasks OWNER TO kyle;

--
-- Name: tasks_id_seq; Type: SEQUENCE; Schema: public; Owner: kyle
--

CREATE SEQUENCE public.tasks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tasks_id_seq OWNER TO kyle;

--
-- Name: tasks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kyle
--

ALTER SEQUENCE public.tasks_id_seq OWNED BY public.tasks.id;


--
-- Name: tasks id; Type: DEFAULT; Schema: public; Owner: kyle
--

ALTER TABLE ONLY public.tasks ALTER COLUMN id SET DEFAULT nextval('public.tasks_id_seq'::regclass);


--
-- Name: tasks tasks_pkey; Type: CONSTRAINT; Schema: public; Owner: kyle
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

\unrestrict fH0eRquJLW1F6djfwWs3FudhyT0csnxwOVrOQyn73tYO8rdNM8blzxo2wCS99TB

