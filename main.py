import easyspa as es


def main():
    args = es.parse_arguments()
    # adict = args.__dict__
    run = es.select_mode(args.mode)
    run(args)


if __name__ == "__main__":
    main()
