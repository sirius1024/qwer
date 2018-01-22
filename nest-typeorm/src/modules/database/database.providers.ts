import { createConnection } from 'typeorm';

export const databaseProviders = [
  {
    provide: 'DbConnectionToken',
    useFactory: async () => await createConnection({
      type: 'mongodb',
      host: 'mongoprod1.test.com',
      port: 27017,
      username: 'sa',
      password: '123456',
      database: 'got-developing',
      entities: [
        __dirname + '/../**/**.entity{.ts,.js}',
      ],
      autoSchemaSync: true,
    }),
  },
];