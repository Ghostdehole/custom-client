FROM python:3.12-slim

RUN groupadd -r appgroup && useradd -r -u 1000 -g appgroup -d /opt/gdpro user

WORKDIR /opt/gdpro

COPY --chown=user:appgroup . .

RUN mkdir -p /opt/gdpro/staticfiles
RUN chown -R user:appgroup /opt/gdpro/staticfiles

RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt

USER user

EXPOSE 9000

CMD ["sh", "-c", "python manage.py collectstatic --noinput && exec gunicorn --config gunicorn.conf.py gdpro.wsgi:application"]














