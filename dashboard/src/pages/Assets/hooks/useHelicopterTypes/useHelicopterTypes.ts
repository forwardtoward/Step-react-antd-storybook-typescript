import assetsQueryKeys from 'api/queryKeys/assets';
import { TenantsService } from 'api/schema';
import useTenant from 'hooks/useTenant';
import { useQuery } from 'react-query';
import { noop } from 'utils/api';

async function fetch({
  page,
  pageSize,
  tenantId,
}: {
  tenantId: number;
  page: number;
  pageSize: number | undefined;
}) {
  const { data } = await TenantsService.tenantsEmissionsHelicopterTypesList(
    tenantId,
    page,
    pageSize,
  );
  return data;
}

const useHelicopterTypes = ({
  page,
  pageSize,
}: {
  page: number;
  pageSize?: number;
}) => {
  const { tenantId } = useTenant();
  const enabled = !!tenantId;

  return useQuery(
    enabled
      ? assetsQueryKeys.helicopterTypes({ tenantId, page, pageSize })
      : [],
    enabled ? () => fetch({ tenantId, page, pageSize }) : noop,
    {
      enabled,
    },
  );
};

export default useHelicopterTypes;
