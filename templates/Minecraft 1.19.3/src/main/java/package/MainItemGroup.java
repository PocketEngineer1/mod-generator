package !mod.java_pkg;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.itemgroup.v1.FabricItemGroup;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;
import net.minecraft.util.Identifier;
import net.minecraft.block.Blocks;

public class MainItemGroup implements ModInitializer {
    ItemGroup mainItemGroup = FabricItemGroup.builder(new Identifier("!mod.id", "stuff"))
    .icon(() -> new ItemStack(Blocks.COBBLESTONE))
    // .entries((enabledFeatures, entries, operatorEnabled) -> {
    //     entries.add(tomato.THIS_ITEM);
    //     entries.add(carrot.THIS_ITEM);
    //     entries.add(peanut_butter.THIS_ITEM);
    // })
    .build();

	@Override
	public void onInitialize() {
	}
}