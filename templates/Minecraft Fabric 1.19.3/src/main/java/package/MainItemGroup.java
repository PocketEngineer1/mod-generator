package !mod.java_pkg;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.itemgroup.v1.FabricItemGroup;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;
import net.minecraft.util.Identifier;
import net.minecraft.block.Blocks;
!item.imports
!block.imports

public class MainItemGroup implements ModInitializer {
    ItemGroup GROUP = FabricItemGroup.builder(new Identifier("!mod.id", "stuff"))
    .icon(() -> new ItemStack(Blocks.COBBLESTONE))
    .entries((enabledFeatures, entries, operatorEnabled) -> {
        !item.entries
        !block.entries
    })
    .build();

	@Override
	public void onInitialize() {
	}
}