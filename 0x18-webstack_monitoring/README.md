# 0x18-webstack_monitoring

## Author

Tadala N. Kapengule

## Tasks

### 0. Sign up for Datadog and install datadog-agent

Install ``datadog-agent`` on ``web-01`` using ``US1``

### 1. Monitor some metrics

Set up some monitors within the ``Datadog`` dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: [System Check](https://docs.datadoghq.com/integrations/system/).


- Set up a monitor that checks the number of read requests issued to the device per second.
- Set up a monitor that checks the number of write requests issued to the device per second.

### 2. Create a dashboard

Now create a dashboard with different metrics displayed in order to get a few different visualizations.

- Create a new ``dashboard``
- Add at least 4 widgets to your dashboard. They can be of any type and monitor whatever you’d like
- Create the answer file ``2-setup_datadog`` which has the ``dashboard_id`` on the first line. Note: in order to get the id of your dashboard, you may need to use Datadog’s API

__File__

``2-setup_datadog``
