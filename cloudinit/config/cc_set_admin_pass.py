from cloudinit import util


def handle(_name, cfg, cloud, log, args):
    admin_pass = cloud.get_admin_pass()
    if not admin_pass:
        log.debug("admin_pass is not in datasource, could not set admin password")
        return

    log.warning("Changing password for admin with admin_pass")
    try:
        util.subp(['chpasswd'], "admin:%s\n" % admin_pass)
    except util.ProcessExecutionError as e:
        util.logexc(log, "chpasswd failed with exit code %d" % e.exit_code)
